from fastapi import APIRouter, Path, Query
from hrone_backend.controllers.order_controller import create_order, get_orders_by_user
from hrone_backend.models.order_model import OrderIn

router = APIRouter()

# POST /orders - create a new order
@router.post("/orders")
def create_order_route(order: OrderIn):
    return create_order(order)

# GET /orders/{user_id} - get all orders by user
@router.get("/orders/{user_id}")
def get_orders_by_user_route(
    user_id: str = Path(..., description="User ID"),
    limit: int = Query(default=10, ge=0),
    offset: int = Query(default=0, ge=0)
):
    return get_orders_by_user(user_id=user_id, limit=limit, offset=offset)
