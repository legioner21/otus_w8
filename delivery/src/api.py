import random

from fastapi import APIRouter
from pydantic import BaseModel

delivery_router = APIRouter()


class Order(BaseModel):
    id: str


@delivery_router.post(
    "/process/delivery/",
)
def process_delivery(
        order: Order,
):
    """
    Процесс доставки:
    """
    return random.choice([True, False])


@delivery_router.post(
    "/rollback/delivery/",
)
def rollback_delivery(
        order: Order,
):
    """
    Процесс отмены доставки:
    """
    return True


api_router = APIRouter()
api_router.include_router(delivery_router, prefix="/delivery", tags=["delivery"])
