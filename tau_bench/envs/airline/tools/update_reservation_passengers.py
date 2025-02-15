# Copyright Sierra

import json
from typing import Any, Dict, List
from tau_bench.envs.tool import Tool


class UpdateReservationPassengers(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        reservation_id: str,
        passengers: List[Dict[str, Any]],
    ) -> str:
        reservations = data["reservations"]
        if reservation_id not in reservations:
            return "Қате: брондау табылмады"
        reservation = reservations[reservation_id]
        if len(passengers) != len(reservation["passengers"]):
            return "Қате: жолаушылар саны сәйкес келмейді"
        reservation["passengers"] = passengers
        return json.dumps(reservation)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_reservation_passengers",
                "description": "Брондаудың жолаушылар туралы ақпаратын жаңарту.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "Брондау идентификаторы, мысалы, 'ZFA04Y'.",
                        },
                        "passengers": {
                            "type": "array",
                            "description": "Әрбір жолаушы туралы мәліметтерді қамтитын объектілер массиві.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "first_name": {
                                        "type": "string",
                                        "description": "Жолаушының аты, мысалы, 'Noah'.",
                                    },
                                    "last_name": {
                                        "type": "string",
                                        "description": "Жолаушының тегі, мысалы, 'Brown'.",
                                    },
                                    "dob": {
                                        "type": "string",
                                        "description": "Жолаушының туған күні 'YYYY-MM-DD' форматында, мысалы, '1990-01-01'.",
                                    },
                                },
                                "required": ["first_name", "last_name", "dob"],
                            },
                        },
                    },
                    "required": ["reservation_id", "passengers"],
                },
            },
        }
