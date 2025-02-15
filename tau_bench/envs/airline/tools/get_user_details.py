# Copyright Sierra

import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool


class GetUserDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        users = data["users"]
        if user_id in users:
            return json.dumps(users[user_id])
        return "Қате: пайдаланушы табылмады."

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Пайдаланушының толық мәліметтерін алыңыз.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Пайдаланушы идентификаторы, мысалы, 'sara_doe_496'.",
                        },
                    },
                    "required": ["user_id"],
                },
            },
        }
