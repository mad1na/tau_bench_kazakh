# Copyright Sierra

from typing import Any, Dict
from tau_bench.envs.tool import Tool


class TransferToHumanAgents(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        summary: str,
    ) -> str:
        return "Аудару сәтті аяқталды."

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transfer_to_human_agents",
                "description": "Пайдаланушыны адам агентіне бағыттаңыз, оның мәселесінің қысқаша сипаттамасымен бірге. Тек пайдаланушы арнайы адам агентін сұрағанда немесе мәселені қолжетімді құралдармен шешу мүмкін болмағанда ғана аударыңыз.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "summary": {
                            "type": "string",
                            "description": "Пайдаланушы мәселесінің қысқаша сипаттамасы.",
                        },
                    },
                    "required": [
                        "summary",
                    ],
                },
            },
        }
