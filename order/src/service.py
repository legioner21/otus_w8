import uuid
from typing import Dict

import requests


class PaymentException(Exception):
    ...


class ReserveException(Exception):
    ...


class DeliveryException(Exception):
    ...


class OrderService:

    def __init__(
            self,
            payment_url: str,
            rollback_payment_url: str,
            reserve_url: str,
            rollback_reserve_url: str,
            delivery_url: str,
            rollback_delivery_url: str,
    ):
        self.payment_url = payment_url
        self.rollback_payment_url = rollback_payment_url
        self.reserve_url = reserve_url
        self.rollback_reserve_url = rollback_reserve_url
        self.delivery_url = delivery_url
        self.rollback_delivery_url = rollback_delivery_url

    def create_order_action(self) -> Dict:
        """Создание заказа. только для показа, не использовать"""

        order_uuid = str(uuid.uuid4())
        item_1_uuid = str(uuid.uuid4())
        item_2_uuid = str(uuid.uuid4())

        return_result = {
            "payment": False,
            "reserve": False,
            "delivery": False,
            "status": False,
            "description": ""
        }
        try:
            try:
                # step1: payment
                try:
                    payment_response = requests.post(self.payment_url, json={'id': order_uuid})
                    payment_response.raise_for_status()
                    payment_result = payment_response.json()
                    if not payment_result:
                        raise PaymentException
                    return_result["payment"] = True

                except Exception as e:
                    raise PaymentException

                # step1: reserve stock
                try:
                    reserve_1_response = requests.post(self.reserve_url,
                                                      json={'id': order_uuid, 'item_id': item_1_uuid})
                    reserve_1_response.raise_for_status()
                    reserve_1_result = reserve_1_response.json()
                    if not reserve_1_result:
                        raise ReserveException

                    reserve_2_response = requests.post(self.reserve_url,
                                                      json={'id': order_uuid, 'item_id': item_2_uuid})
                    reserve_2_response.raise_for_status()
                    reserve_2_result = reserve_2_response.json()
                    if not reserve_2_result:
                        raise ReserveException

                    return_result["reserve"] = True
                except Exception as e:
                    raise ReserveException

                # step1: delivery
                try:
                    delivery_response = requests.post(self.delivery_url, json={'id': order_uuid})
                    delivery_response.raise_for_status()
                    delivery_result = delivery_response.json()
                    if not delivery_result:
                        raise DeliveryException
                    return_result["delivery"] = True
                except Exception as e:
                    raise DeliveryException

            except PaymentException as e:
                return_result["description"] = "Ошибка при оплате"
                return return_result

            except ReserveException as e:
                requests.post(self.rollback_payment_url, json={'id': order_uuid})
                return_result["description"] = "Ошибка при резервировании"
                return return_result

            except DeliveryException as e:
                requests.post(self.rollback_payment_url, json={'id': order_uuid})
                requests.post(self.rollback_reserve_url, json={'id': order_uuid})
                return_result["description"] = "Ошибка при создании доставки"
                return return_result

        except Exception as e:
            return_result["description"] = "Ошибка при создании заказа"
            return return_result

        return_result["description"] = "Успешное создание заказа"
        return_result["status"] = True
        return return_result
