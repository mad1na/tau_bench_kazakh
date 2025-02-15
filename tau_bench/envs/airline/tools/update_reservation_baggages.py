# Copyright Sierra

import json
from typing import Any, Dict
from tau_bench.envs.tool import Tool


class UpdateReservationBaggages(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        reservation_id: str,
        total_baggages: int,
        nonfree_baggages: int,
        payment_id: str,
    ) -> str:
        users, reservations = data["users"], data["reservations"]
        if reservation_id not in reservations:
            return "Қате: брондау табылмады"
        reservation = reservations[reservation_id]

        total_price = 50 * max(0, nonfree_baggages - reservation["nonfree_baggages"])
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

        reservation["total_baggages"] = total_baggages
        reservation["nonfree_baggages"] = nonfree_baggages
        if payment_method["source"] == "gift_card":
            payment_method["amount"] -= total_price

        if total_price != 0:
            reservation["payment_history"].append(
                {
                    "payment_id": payment_id,
                    "amount": total_price,
                }
            )

        return json.dumps(reservation)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_reservation_baggages",
                "description": "Брондаудың жүк туралы ақпаратын жаңарту.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "Брондау идентификаторы, мысалы, 'ZFA04Y'.",
                        },
                        "total_baggages": {
                            "type": "integer",
                            "description": "Брондауға енгізілген жалпы жүк санын жаңарту.",
                        },
                        "nonfree_baggages": {
                            "type": "integer",
                            "description": "Брондауға енгізілген ақылы жүк санын жаңарту.",
                        },
                        "payment_id": {
                            "type": "string",
                            "description": "Пайдаланушы профилінде сақталған төлем идентификаторы, мысалы, 'credit_card_7815826', 'gift_card_7815826', 'certificate_7815826'.",
                        },
                    },
                    "required": [
                        "reservation_id",
                        "total_baggages",
                        "nonfree_baggages",
                        "payment_id",
                    ],
                },
            },
        }
