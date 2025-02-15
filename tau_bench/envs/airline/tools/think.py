# Copyright Sierra

from typing import Any, Dict
from tau_bench.envs.tool import Tool


class Think(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], thought: str) -> str:
        return ""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "think",
                "description": "Құралды ойлану үшін пайдаланыңыз. Ол жаңа ақпарат алмайды немесе дерекқорды өзгертпейді, тек ойды журналға қосады. Күрделі ойлау қажет болғанда оны пайдаланыңыз.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thought": {
                            "type": "string",
                            "description": "Ойланатын ой.",
                        },
                    },
                    "required": ["thought"],
                },
            },
        }
