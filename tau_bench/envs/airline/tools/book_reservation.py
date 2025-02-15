# Copyright Sierra

import json
from copy import deepcopy
from typing import Any, Dict, List
from tau_bench.envs.tool import Tool


class BookReservation(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        user_id: str,
        origin: str,
        destination: str,
        flight_type: str,
        cabin: str,
        flights: List[Dict[str, Any]],
        passengers: List[Dict[str, Any]],
        payment_methods: List[Dict[str, Any]],
        total_baggages: int,
        nonfree_baggages: int,
        insurance: str,
    ) -> str:
        reservations, users = data["reservations"], data["users"]
        if user_id not in users:
            return "Қате: пайдаланушы табылмады"
        user = users[user_id]

        # assume each task makes at most 3 reservations
        reservation_id = "HATHAT"
        if reservation_id in reservations:
            reservation_id = "HATHAU"
            if reservation_id in reservations:
                reservation_id = "HATHAV"

        reservation = {
            "reservation_id": reservation_id,
            "user_id": user_id,
            "origin": origin,
            "destination": destination,
            "flight_type": flight_type,
            "cabin": cabin,
            "flights": deepcopy(flights),
            "passengers": passengers,
            "payment_history": payment_methods,
            "created_at": "2024-05-15T15:00:00",
            "total_baggages": total_baggages,
            "nonfree_baggages": nonfree_baggages,
            "insurance": insurance,
        }

        # update flights and calculate price
        total_price = 0
        for flight in reservation["flights"]:
            flight_number = flight["flight_number"]
            if flight_number not in data["flights"]:
                return f"Қате: {flight_number} рейсі табылмады"
            flight_data = data["flights"][flight_number]
            if flight["date"] not in flight_data["dates"]:
                return f"Қате: {flight_number} рейсі {flight['date']} күнінде қолжетімсіз"
            flight_date_data = flight_data["dates"][flight["date"]]
            if flight_date_data["status"] != "available":
                return f"Қате: {flight_number} рейсі қолжетімсіз"
            if flight_date_data["available_seats"][cabin] < len(passengers):
                return f"Қате: {flight_number} рейсінде жеткілікті орын жоқ"
            flight["price"] = flight_date_data["prices"][cabin]
            flight["origin"] = flight_data["origin"]
            flight["destination"] = flight_data["destination"]
            total_price += flight["price"] * len(passengers)

        if insurance == "yes":
            total_price += 30 * len(passengers)

        total_price += 50 * nonfree_baggages

        for payment_method in payment_methods:
            payment_id = payment_method["payment_id"]
            amount = payment_method["amount"]
            if payment_id not in user["payment_methods"]:
                return f"Қате: {payment_id} төлем әдісі табылмады"
            if user["payment_methods"][payment_id]["source"] in [
                "gift_card",
                "certificate",
            ]:
                if user["payment_methods"][payment_id]["amount"] < amount:
                    return f"Қате: {payment_id} төлем әдісінде жеткілікті қаражат жоқ"
        if sum(payment["amount"] for payment in payment_methods) != total_price:
            return f"Қате: төлем сомасы сәйкес келмейді, жалпы баға {total_price}, төленген {sum(payment['amount'] for payment in payment_methods)}"

        # if checks pass, deduct payment and update seats
        for payment_method in payment_methods:
            payment_id = payment_method["payment_id"]
            amount = payment_method["amount"]
            if user["payment_methods"][payment_id]["source"] == "gift_card":
                user["payment_methods"][payment_id]["amount"] -= amount
            elif user["payment_methods"][payment_id]["source"] == "certificate":
                del user["payment_methods"][payment_id]

        reservations[reservation_id] = reservation
        user["reservations"].append(reservation_id)
        return json.dumps(reservation)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "book_reservation",
                "description": "Әуе рейсіне брондау жасау.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Пайдаланушының ID-і., мысалы 'aidos_aidosov_6400'.",
                        },
                        "origin": {
                            "type": "string",
                            "description": "Бастапқы қаланың IATA коды., мысалы 'ALA'.",
                        },
                        "destination": {
                            "type": "string",
                            "description": "Мақсатты қаланың IATA коды., мысалы 'NQZ'.",
                        },
                        "flight_type": {
                            "type": "string",
                            "enum": ["one_way", "round_trip"],
                        },
                        "cabin": {
                            "type": "string",
                            "enum": [
                                "basic_economy",
                                "economy",
                                "business",
                            ],
                        },
                        "flights": {
                            "type": "array",
                            "description": "Әр рейс туралы мәліметтер.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "flight_number": {
                                        "type": "string",
                                        "description": "Рейс нөмірі, мысалы, 'HAT001'.",
                                    },
                                    "date": {
                                        "type": "string",
                                        "description": "Ұшу күні 'YYYY-MM-DD' форматында, мысалы, '2024-05-01'.",
                                    },
                                },
                                "required": ["flight_number", "date"],
                            },
                        },
                        "passengers": {
                            "type": "array",
                            "description": "Жолаушылар тізімі.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "first_name": {
                                        "type": "string",
                                        "description": "Жолаушының аты, мысалы, 'Нұрахан'.",
                                    },
                                    "last_name": {
                                        "type": "string",
                                        "description": "Жолаушының тегі, мысалы, 'Абаев'.",
                                    },
                                    "dob": {
                                        "type": "string",
                                        "description": "Жолаушының туған күні 'YYYY-MM-DD' форматында, мысалы, '1990-01-01'.",
                                    },
                                },
                                "required": ["first_name", "last_name", "dob"],
                            },
                        },
                        "payment_methods": {
                            "type": "array",
                            "description": "Төлем әдістерінің тізімі.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "payment_id": {
                                        "type": "string",
                                        "description": "Пайдаланушы профилінде сақталған төлем идентификаторы, мысалы, 'credit_card_7815826', 'gift_card_7815826', 'certificate_7815826'.",
                                    },
                                    "amount": {
                                        "type": "number",
                                        "description": "Төленуі қажет сома.",
                                    },
                                },
                                "required": ["payment_id", "amount"],
                            },
                        },
                        "total_baggages": {
                            "type": "integer",
                            "description": "Брондауға кіретін багаж заттарының жалпы саны.",
                        },
                        "nonfree_baggages": {
                            "type": "integer",
                            "description": "Брондауға кіретін ақылы багаж заттарының саны.",
                        },
                        "insurance": {
                            "type": "string",
                            "enum": ["yes", "no"],
                        },
                    },
                    "required": [
                        "user_id",
                        "origin",
                        "destination",
                        "flight_type",
                        "cabin",
                        "flights",
                        "passengers",
                        "payment_methods",
                        "total_baggages",
                        "nonfree_baggages",
                        "insurance",
                    ],
                },
            },
        }
