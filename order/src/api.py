from fastapi import APIRouter

from app_config import settings
from service import OrderService

order_router = APIRouter()


@order_router.post(
    "/creating/",
)
def creating():
    """
    Процесс создания заказа:
    """
    order_service: OrderService = OrderService(
        payment_url=settings.ORDER_PAYMENT_URL,
        rollback_payment_url=settings.ORDER_ROLLBACK_PAYMENT_URL,
        reserve_url=settings.ORDER_RESERVE_URL,
        rollback_reserve_url=settings.ORDER_ROLLBACK_RESERVE_URL,
        delivery_url=settings.ORDER_DELIVERY_URL,
        rollback_delivery_url=settings.ORDER_ROLLBACK_DELIVERY_URL,
    )
    return order_service.create_order_action()


api_router = APIRouter()
api_router.include_router(order_router, prefix="/order", tags=["order"])
