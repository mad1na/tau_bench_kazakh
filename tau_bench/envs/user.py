# Copyright Sierra

import abc
import enum
from litellm import completion

from typing import Optional, List, Dict, Any, Union


class BaseUserSimulationEnv(abc.ABC):
    metadata = {}

    @abc.abstractmethod
    def reset(self, instruction: Optional[str] = None) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def step(self, content: str) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def get_total_cost(self) -> float:
        raise NotImplementedError


class HumanUserSimulationEnv(BaseUserSimulationEnv):
    def reset(self, instruction: str) -> str:
        return input(f"{instruction}\n")

    def step(self, content: str) -> str:
        return input(f"{content}\n")

    def get_total_cost(self) -> float:
        return 0


class LLMUserSimulationEnv(BaseUserSimulationEnv):
    def __init__(self, model: str, provider: str) -> None:
        super().__init__()
        self.messages: List[Dict[str, Any]] = []
        self.model = model
        self.provider = provider
        self.total_cost = 0.0
        self.reset()

    def generate_next_message(self, messages: List[Dict[str, Any]]) -> str:
        res = completion(
            model=self.model, custom_llm_provider=self.provider, messages=messages
        )
        message = res.choices[0].message
        self.messages.append(message.model_dump())
        self.total_cost = res._hidden_params["response_cost"]
        return message.content

    def build_system_prompt(self, instruction: Optional[str]) -> str:
        instruction_display = (
            ("\n\nInstruction: " + instruction + "\n")
            if instruction is not None
            else ""
        )
        return f"""Сіз агентпен әрекеттесетін пайдаланушысыз.{instruction_display}
Ережелер:

- Пайдаланушының хабарламасын бір жолдан ғана жасаңыз.
- Барлық нұсқауларды бірден бермеңіз. Тек ағымдағы қадам үшін қажетті ақпаратты ғана ұсыныңыз.
- Нұсқауда берілмеген ақпаратты ойдан шығармаңыз. Мысалы, егер агент тапсырыс идентификаторын сұраса, бірақ ол нұсқауда жоқ болса, оны ойлап таппай, есіңізде жоқ немесе қолыңызда жоқ екенін айтыңыз.
- Егер нұсқаулықтың мақсаты орындалса, әңгімені аяқтау үшін жеке жолда тек '###STOP###' деп жазыңыз.
- Нақты нұсқауларды қайталамаңыз, оның орнына сол мағынаны өз сөзіңізбен жеткізіңіз.
- Әңгімеңізді мүмкіндігінше табиғи етіп құрыңыз және нұсқауда берілген тұлғалық ерекшеліктерге сәйкестендіріңіз."""

    def reset(self, instruction: Optional[str] = None) -> str:
        self.messages = [
            {
                "role": "system",
                "content": self.build_system_prompt(instruction=instruction),
            },
            {"role": "user", "content": "Сәлем! Сізге бүгін қалай көмектесе аламын?"},
        ]
        return self.generate_next_message(self.messages)

    def step(self, content: str) -> str:
        self.messages.append({"role": "user", "content": content})
        return self.generate_next_message(self.messages)

    def get_total_cost(self) -> float:
        return self.total_cost


class ReactUserSimulationEnv(LLMUserSimulationEnv):
    def __init__(self, model: str, provider: str) -> None:
        super().__init__(model=model, provider=provider)
        self.reset()

    def build_system_prompt(self, instruction: Optional[str]) -> str:
        instruction_display = (
            ("\n\nInstruction: " + instruction + "\n")
            if instruction is not None
            else ""
        )
        return f"""Сіз агентпен әрекеттесетін пайдаланушысыз.{instruction_display}
Ережелер:

- Алдымен, келесі әрекет туралы ой жасаңыз (бұл хабарлама агентке жіберілмейді).
- Содан кейін, пайдаланушының агентке жіберілетін бір жолдық жауабын жасаңыз.
- Барлық ақпаратты бірден бермеңіз. Тек сол қадам үшін қажетті мәліметтерді ғана ұсыныңыз.
- Нұсқауда жоқ ақпаратты ойдан шығармаңыз. Егер агент сізден тапсырыс идентификаторын сұраса, бірақ ол нұсқауда болмаса, онда есіңізде жоқ немесе қолыңызда жоқ екенін айтыңыз.
- Егер нұсқаулықтағы мақсат орындалса, әңгімені аяқтау үшін '###STOP###' деп жеке жолда жазыңыз.
- Нақты нұсқауларды қайталамаңыз, оның орнына сол мағынаны өз сөзіңізбен жеткізіңіз.
- Әңгімеңізді табиғи етіп құрыңыз және нұсқауда берілген тұлғалық ерекшеліктерге сәйкестендіріңіз.

Формат:

Ой:
<мұнда ойды жазыңыз>

Пайдаланушы жауабы:
<пайдаланушының агентке жіберілетін жауабы>"""

    def generate_next_message(self, messages: List[Dict[str, Any]]) -> str:
        res = completion(
            model=self.model, custom_llm_provider=self.provider, messages=messages
        )
        message = res.choices[0].message
        self.messages.append(message.model_dump())
        self.total_cost = res._hidden_params["response_cost"]
        return self.parse_response(message.content)

    def reset(self, instruction: Optional[str] = None) -> str:
        self.messages = [
            {
                "role": "system",
                "content": self.build_system_prompt(instruction=instruction),
            },
            {"role": "user", "content": "Сәлем! Сізге бүгін қалай көмектесе аламын?"},
        ]
        return self.generate_next_message(self.messages)

    def parse_response(self, response: str) -> str:
        if "###STOP###" in response:
            return "###STOP###"
        elif "Thought:" in response:
            _, user_response = response.split("Ой:")
            return user_response.strip()
        elif "User Response:" in response:
            _, user_response = response.split("Пайдаланушы жауабы:")
            return user_response.strip()
        else:
            raise ValueError(f"Жарамсыз жауап форматы:{response}")

    def step(self, content: str) -> str:
        self.messages.append({"role": "user", "content": content})
        return self.generate_next_message(self.messages)

    def get_total_cost(self) -> float:
        return self.total_cost


class VerifyUserSimulationEnv(LLMUserSimulationEnv):
    def __init__(self, model: str, provider: str, max_attempts: int = 3) -> None:
        self.model = model
        self.provider = provider
        self.max_attempts = max_attempts
        self.reset()

    def generate_next_message(self, messages: List[Dict[str, Any]]) -> str:
        attempts = 0
        cur_message = None
        while attempts < self.max_attempts:
            res = completion(
                model=self.model, custom_llm_provider=self.provider, messages=messages
            )
            cur_message = res.choices[0].message
            self.total_cost = res._hidden_params["response_cost"]
            if verify(self.model, self.provider, cur_message, messages):
                self.messages.append(cur_message.model_dump())
                return cur_message.content
            attempts += 1
        assert cur_message is not None
        return cur_message.content

    def reset(self, instruction: Optional[str] = None) -> str:
        self.messages = [
            {
                "role": "system",
                "content": self.build_system_prompt(instruction=instruction),
            },
            {"role": "user", "content": "Сәлем! Сізге бүгін қалай көмектесе аламын?"},
        ]
        return self.generate_next_message(self.messages)

    def step(self, content: str) -> str:
        self.messages.append({"role": "user", "content": content})
        return self.generate_next_message(self.messages)

    def get_total_cost(self) -> float:
        return self.total_cost


def map_role_label(role: str) -> str:
    if role == "user":
        return "Customer"
    elif role == "assistant":
        return "Agent"
    else:
        return role.capitalize()


def verify(
    model: str, provider: str, response: str, messages: List[Dict[str, Any]]
) -> bool:
    transcript = "\n".join(
        [
            f"{map_role_label(message['role'])}: {message['content']}"
            for message in messages
        ]
    )
    prompt = f"""Сіз әңгімедегі Агенттің супервайзерісіз. Сізге Тұтынушы мен Агент арасындағы әңгіменің транскрипті беріледі. Тұтынушының Жауабы жасалған, және сіз оның қанағаттанарлық екенін (true) немесе қанағаттанарлық емес екенін (false) тексеруіңіз керек.
Сіздің жауабыңыз талданады, сондықтан тек классификацияны (true немесе false) ғана жазыңыз, басқа ешқандай мәтін қоспаңыз.
    
# Транскрипт:
{transcript}

# Жауап:
{response}

-----

Классификация:"""
    res = completion(
        model=model,
        custom_llm_provider=provider,
        messages=[{"role": "user", "content": prompt}],
    )
    return "true" in res.choices[0].message.content.lower()


def reflect(
    model: str, provider: str, response: str, messages: List[Dict[str, Any]]
) -> str:
    transcript = "\n".join(
        [
            f"{map_role_label(message['role'])}: {message['content']}"
            for message in messages
        ]
    )
    prompt = f"""Сіз әңгімедегі Агенттің супервайзерісіз. Сізге (симуляцияланған) Тұтынушы мен Агент арасындағы әңгіменің транскрипті беріледі. Тұтынушының Жауабы сіз тарапынан қанағаттанарлықсыз деп бағаланды.
Сіз әңгіменің қай жерінде қате кеткенін талдап, оны түзету үшін жаңа Жауап ұсынуыңыз керек.
Сіздің жауабыңыз талданады, сондықтан тек классификацияны (true немесе false) ғана жазыңыз, басқа ешқандай мәтін қоспаңыз.
    
# Транскрипт:
{transcript}

# Жауап:
{response}

# Формат:

Рефлексия:
<қате кеткен жерлер туралы талдау>

Жауап:
<агентке жіберілетін түзетілген жауап>"""
    res = completion(
        model=model,
        custom_llm_provider=provider,
        messages=[{"role": "user", "content": prompt}],
    )
    _, response = res.choices[0].message.content.split("Response:")
    return response.strip()


class ReflectionUserSimulationEnv(LLMUserSimulationEnv):
    def __init__(self, model: str, provider: str, max_attempts: int = 2) -> None:
        self.model = model
        self.provider = provider
        self.max_attempts = max_attempts
        self.reset()

    def generate_next_message(self, messages: List[Dict[str, Any]]) -> str:
        cur_messages = messages.copy()
        initial_response = super().generate_next_message(cur_messages)
        if verify(self.model, self.provider, initial_response, cur_messages):
            return initial_response
        attempts = 1
        while attempts < self.max_attempts:
            new_message = reflect(
                self.model, self.provider, initial_response, cur_messages
            )
            cur_messages.append({"role": "user", "content": new_message})
            new_response = super().generate_next_message(cur_messages)
            if verify(self.model, self.provider, new_response, cur_messages):
                return new_response
            attempts += 1
        return initial_response

    def reset(self, instruction: Optional[str] = None) -> str:
        self.messages = [
            {
                "role": "system",
                "content": self.build_system_prompt(instruction=instruction),
            },
            {"role": "user", "content": "Сәлем! Сізге бүгін қалай көмектесе аламын?"},
        ]
        return self.generate_next_message(self.messages)

    def step(self, content: str) -> str:
        self.messages.append({"role": "user", "content": content})
        return self.generate_next_message(self.messages)

    def get_total_cost(self) -> float:
        return self.total_cost


class UserStrategy(enum.Enum):
    HUMAN = "human"
    LLM = "llm"
    REACT = "react"
    VERIFY = "verify"
    REFLECTION = "reflection"


def load_user(
    user_strategy: Union[str, UserStrategy],
    model: Optional[str] = "gpt-4o",
    provider: Optional[str] = None,
) -> BaseUserSimulationEnv:
    if isinstance(user_strategy, str):
        user_strategy = UserStrategy(user_strategy)
    if user_strategy == UserStrategy.HUMAN:
        return HumanUserSimulationEnv()
    elif user_strategy == UserStrategy.LLM:
        if model is None:
            raise ValueError("LLM user strategy requires a model")
        if provider is None:
            raise ValueError("LLM user strategy requires a model provider")
        return LLMUserSimulationEnv(model=model, provider=provider)
    elif user_strategy == UserStrategy.REACT:
        if model is None:
            raise ValueError("React user strategy requires a model")
        if provider is None:
            raise ValueError("React user strategy requires a model provider")
        return ReactUserSimulationEnv(model=model, provider=provider)
    elif user_strategy == UserStrategy.VERIFY:
        if model is None:
            raise ValueError("Verify user strategy requires a model")
        if provider is None:
            raise ValueError("Verify user strategy requires a model provider")
        return VerifyUserSimulationEnv(model=model, provider=provider)
    elif user_strategy == UserStrategy.REFLECTION:
        if model is None:
            raise ValueError("Reflection user strategy requires a model")
        if provider is None:
            raise ValueError("Reflection user strategy requires a model provider")
        return ReflectionUserSimulationEnv(model=model, provider=provider)
    raise ValueError(f"Unknown user strategy {user_strategy}")
