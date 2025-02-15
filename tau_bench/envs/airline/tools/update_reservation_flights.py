# Copyright Sierra

import json
from copy import deepcopy
from typing import Any, Dict, List
from tau_bench.envs.tool import Tool


class UpdateReservationFlights(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        reservation_id: str,
        cabin: str,
        flights: List[Dict[str, Any]],
        payment_id: str,
    ) -> str:
        users, reservations = data["users"], data["reservations"]
        if reservation_id not in reservations:
            return "Қате: брондау табылмады"
        reservation = reservations[reservation_id]

        # update flights and calculate price
        total_price = 0
        flights = deepcopy(flights)
        for flight in flights:
            # if existing flight, ignore
            if _ := [
                f
                for f in reservation["flights"]
                if f["flight_number"] == flight["flight_number"]
                and f["date"] == flight["date"]
                and cabin == reservation["cabin"]
            ]:
                total_price += _[0]["price"] * len(reservation["passengers"])
                flight["price"] = _[0]["price"]
                flight["origin"] = _[0]["origin"]
                flight["destination"] = _[0]["destination"]
                continue
            flight_number = flight["flight_number"]
            if flight_number not in data["flights"]:
                return f"Қате: {flight_number} рейсі табылмады"
            flight_data = data["flights"][flight_number]
            if flight["date"] not in flight_data["dates"]:
                return f"Қате: {flight_number} рейсі {flight['date']} күні табылмады"
            flight_date_data = flight_data["dates"][flight["date"]]
            if flight_date_data["status"] != "available":
                return f"Қате: {flight_number} рейсі {flight['date']} күні қолжетімді емес"
            if flight_date_data["available_seats"][cabin] < len(
                reservation["passengers"]
            ):
                return f"Қате: {flight_number} рейсінде жеткілікті орын жоқ"
            flight["price"] = flight_date_data["prices"][cabin]
            flight["origin"] = flight_data["origin"]
            flight["destination"] = flight_data["destination"]
            total_price += flight["price"] * len(reservation["passengers"])

        total_price -= sum(flight["price"] for flight in reservation["flights"]) * len(
            reservation["passengers"]
        )

        # check payment
        if payment_id not in users[reservation["user_id"]]["payment_methods"]:
            return "Қате: төлем әдісі табылмады"
        payment_method = users[reservation["user_id"]]["payment_methods"][payment_id]
        if payment_method["source"] == "certificate":
            return "Қате: сертификатты брондауды жаңарту үшін қолдануға болмайды"
        elif (
            payment_method["source"] == "gift_card"
            and payment_method["amount"] < total_price
        ):
            return "Қате: сыйлық картадағы баланс жеткіліксіз"

        # if checks pass, deduct payment and update seats
        if payment_method["source"] == "gift_card":
            payment_method["amount"] -= total_price
        reservation["flights"] = flights
        if total_price != 0:
            reservation["payment_history"].append(
                {
                    "payment_id": payment_id,
                    "amount": total_price,
                }
            )
        # do not make flight database update here, assume it takes time to be updated
        return json.dumps(reservation)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_reservation_flights",
                "description": "Брондаудың рейс туралы ақпаратын жаңарту.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "Брондау идентификаторы, мысалы, 'ZFA04Y'.",
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
                            "description": "Жаңа брондаудағы әрбір рейс туралы мәліметтерді қамтитын объектілер массиві. Егер рейс өзгермесе де, ол массивте болуы керек.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "flight_number": {
                                        "type": "string",
                                        "description": "Рейс нөмірі, мысалы, 'HAT001'.",
                                    },
                                    "date": {
                                        "type": "string",
                                        "description": "Рейс күні 'YYYY-MM-DD' форматында, мысалы, '2024-05-01'.",
                                    },
                                },
                                "required": ["flight_number", "date"],
                            },
                        },
                        "payment_id": {
                            "type": "string",
                            "description": "Пайдаланушы профилінде сақталған төлем идентификаторы, мысалы, 'credit_card_7815826', 'gift_card_7815826', 'certificate_7815826'.",
                        },
                    },
                    "required": ["reservation_id", "cabin", "flights", "payment_id"],
                },
            },
        }
