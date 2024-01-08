import random

from fastapi import APIRouter
from pydantic import BaseModel

payment_router = APIRouter()


class Order(BaseModel):
    id: str


@payment_router.post(
    "/process/payment/",
)
def process_payment(
        order: Order,
):
    """
    Процесс оплаты:
    """
    return random.choice([True, False])


@payment_router.post(
    "/rollback/payment/",
)
def rollback_payment(
        order: Order,
):
    """
    Процесс отмены оплаты:
    """
    return True


api_router = APIRouter()
api_router.include_router(payment_router, prefix="/payment", tags=["payment"])
