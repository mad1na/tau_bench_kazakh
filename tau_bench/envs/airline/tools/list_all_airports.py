# Copyright Sierra

import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool


class ListAllAirports(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        airports = [
            "ALA",
            "GUW",
            "NQZ",
            "PPK",
            "PWQ",
            "CIT",
            "AKX",
            "UKK",
            "KZO",
            "SCO",
            "URA",
            "DMB",
            "KSN",
            "MSP",
            "DTW",
            "PHL",
            "LGA",
        ]
        cities = [
            "Алматы",
            "Атырау",
            "Астана",
            "Петропавл",
            "Павлодар",
            "Шымкент",
            "Ақтөбе",
            "Өскемен",
            "Қызылорда",
            "Ақтау",
            "Орал",
            "Тараз",
            "Қостанай",
        ]
        return json.dumps({airport: city for airport, city in zip(airports, cities)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_all_airports",
                "description": "Барлық әуежайлар мен олардың қалаларының тізімін келтіріңіз.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
        }
