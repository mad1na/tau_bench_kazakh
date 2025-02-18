# Copyright Sierra

import json
from litellm import completion

from tau_bench.agents.base import Agent
from tau_bench.envs.base import Env
from tau_bench.types import (
    Action,
    SolveResult,
    RESPOND_ACTION_NAME,
    RESPOND_ACTION_FIELD_NAME,
)
from typing import Optional, List, Dict, Any, Tuple


class ChatReActAgent(Agent):
    def __init__(
        self,
        tools_info: List[Dict[str, Any]],
        wiki: str,
        model: str,
        provider: str,
        use_reasoning: bool = True,
        temperature: float = 0.0,
    ) -> None:
        instruction = REACT_INSTRUCTION if use_reasoning else ACT_INSTRUCTION
        self.prompt = (
            wiki + "\n#Available tools\n" + json.dumps(tools_info) + instruction
        )
        self.model = model
        self.provider = provider
        self.temperature = temperature
        self.use_reasoning = use_reasoning
        self.tools_info = tools_info

    def generate_next_step(
        self, messages: List[Dict[str, Any]]
    ) -> Tuple[Dict[str, Any], Action, float]:
        res = completion(
            model=self.model,
            custom_llm_provider=self.provider,
            messages=messages,
            temperature=self.temperature,
        )
        message = res.choices[0].message
        action_str = message.content.split("Action:")[-1].strip()
        try:
            action_parsed = json.loads(action_str)
        except json.JSONDecodeError:
            # this is a hack
            action_parsed = {
                "name": RESPOND_ACTION_NAME,
                "arguments": {RESPOND_ACTION_FIELD_NAME: action_str},
            }
        assert "name" in action_parsed
        assert "arguments" in action_parsed
        action = Action(name=action_parsed["name"], kwargs=action_parsed["arguments"])
        return message.model_dump(), action, res._hidden_params["response_cost"]

    def solve(
        self, env: Env, task_index: Optional[int] = None, max_num_steps: int = 30
    ) -> SolveResult:
        response = env.reset(task_index=task_index)
        reward = 0.0
        messages: List[Dict[str, Any]] = [
            {"role": "system", "content": self.prompt},
            {"role": "user", "content": response.observation},
        ]
        total_cost = 0.0
        info = {}
        for _ in range(max_num_steps):
            message, action, cost = self.generate_next_step(messages)
            response = env.step(action)
            obs = response.observation
            reward = response.reward
            info = {**info, **response.info.model_dump()}
            if action.name != RESPOND_ACTION_NAME:
                obs = "API output: " + obs
            messages.extend(
                [
                    message,
                    {"role": "user", "content": obs},
                ]
            )
            total_cost += cost
            if response.done:
                break
        return SolveResult(
            messages=messages,
            reward=reward,
            info=info,
        )


REACT_INSTRUCTION = f"""
# Нұсқаулық  
Сіз жоғарыда көрсетілген құралдарды пайдаланып, пайдаланушыға жоғарыдағы саясатқа сәйкес көмек көрсететін агент ретінде әрекет етуіңіз керек.  

Әр қадамда сіздің жауабыңыз дәл келесі форматта болуы тиіс:  
**Ой:**  
<Контекстті өңдеп, шешім қабылдауға арналған бір жолдық логикалық ой. Қосымша жолдар қоспаңыз.>  
**Әрекет:**  
{{"name": <Әрекеттің атауы>, "arguments": <Әрекетке арналған аргументтер JSON форматында>}}  

**Әрекет** JSON ретінде талданады, сондықтан оның дұрыс пішімделгеніне көз жеткізіңіз.  

Сіз ойдан шығарылған немесе уақытша аргументтерді қолданбауыңыз керек.  

Мысалы, егер пайдаланушы: **"Мен Сан-Францискодағы ауа райын білгім келеді"** деп сұраса және келесі құрал қолжетімді болса:  
```json
{{
    "type": "function",
    "function": {{
        "name": "get_current_weather",
        "description": "Ауа райын алу",
        "parameters": {{
            "type": "object",
            "properties": {{
                "location": {{
                    "type": "string",
                    "description": "Қала мен штат, мысалы, Сан-Франциско, CA",
                }}},
                "format": {{
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"],
                    "description": "Температура бірлігі. Оны пайдаланушының орналасқан жеріне қарай анықтаңыз.",
                }}}
            }}},
            "required": ["location", "format"],
        }}}
    }}
}}

Сіздің жауабыңыз келесідей болуы мүмкін:
Ой:  
Пайдаланушы АҚШ-тағы Сан-Францискодағы ауа райын сұрады, сондықтан температура бірлігі фаренгейт болуы керек. Мен "get_current_weather" құралын пайдаланып, ақпарат ала аламын.  
Әрекет:  
{{"name": "get_current_weather", "arguments": {{"location": "San Francisco, CA", "format": "fahrenheit"}}}}  

Егер құрал "70F" деп жауап берсе, сіздің жауабыңыз келесідей болуы мүмкін:
Ой:  
Мен енді пайдаланушыға жауап бере аламын.  
Әрекет:  
{{"name": {RESPOND_ACTION_NAME}, "arguments": {{"{RESPOND_ACTION_FIELD_NAME}": "Сан-Францискодағы қазіргі ауа райы 70°F."}}}}  

Пайдаланушыға барынша пайдалы болуға тырысыңыз және саясатты әрдайым ұстаныңыз.
"""


ACT_INSTRUCTION = f"""
# Нұсқаулық
Сіз жоғарыда көрсетілген құралдарды пайдаланып, пайдаланушыға жоғарыдағы саясатқа сәйкес көмек көрсететін агент ретінде әрекет етуіңіз керек.

Әр қадамда сіздің жауабыңыз дәл келесі форматта болуы тиіс:

Әрекет:
{{"name": <Әрекеттің атауы>, "arguments": <Әрекетке арналған аргументтер JSON форматында>}}

Сіз ойдан шығарылған немесе уақытша аргументтерді қолданбауыңыз керек.

Әрекет JSON ретінде талданады, сондықтан оның дұрыс пішімделгеніне көз жеткізіңіз.

Мысалы, егер пайдаланушы "Мен Сан-Францискодағы ауа райын білгім келеді" деп сұраса және келесі құрал қолжетімді болса:
```json
{{
    "type": "function",
    "function": {{
        "name": "get_current_weather",
        "description": "Ауа райын алу",
        "parameters": {{
            "type": "object",
            "properties": {{
                "location": {{
                    "type": "string",
                    "description": "Қала мен штат, мысалы, Сан-Франциско, CA",
                }}},
                "format": {{
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"],
                    "description": "Температура бірлігі. Оны пайдаланушының орналасқан жеріне қарай анықтаңыз.",
                }}}
            }}},
            "required": ["location", "format"],
        }}}
    }}
}}

```

Сіздің жауабыңыз келесідей болуы мүмкін:
Әрекет:  
{{"name": "get_current_weather", "arguments": {{"location": "San Francisco, CA", "format": "fahrenheit"}}}}  

Егер құрал "70F" деп жауап берсе, сіздің жауабыңыз келесідей болуы мүмкін:
Әрекет:  
{{"name": {RESPOND_ACTION_NAME}, "arguments": {{"{RESPOND_ACTION_FIELD_NAME}": "Сан-Францискодағы қазіргі ауа райы 70°F."}}}}  

Пайдаланушыға барынша пайдалы болуға тырысыңыз. Әрқашан тек дұрыс пішімделген JSON жасаңыз.
"""
