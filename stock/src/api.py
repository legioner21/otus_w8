import random

from fastapi import APIRouter
from pydantic import BaseModel

stock_router = APIRouter()


class OrderItem(BaseModel):
    id: str
    item_id: str


@stock_router.post(
    "/process/reserve/",
)
def process_reserve(
        order: OrderItem,
):
    """
    Процесс резервирования:
    """
    return random.choice([True, False])


@stock_router.post(
    "/rollback/reserve/",
)
def rollback_reserve(
        order: OrderItem,
):
    """
    Процесс отмены резервирования:
    """
    return True


api_router = APIRouter()
api_router.include_router(stock_router, prefix="/stock", tags=["stock"])
