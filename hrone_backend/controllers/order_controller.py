from typing import List, Dict, Any
from fastapi import HTTPException
from bson import ObjectId

from hrone_backend.db import orders_col, products_col
from hrone_backend.models.order_model import OrderIn
from hrone_backend.utils import is_valid_objectid


#POST /orders
def create_order(order: OrderIn):
    try:
        user_id = order.userId
        items = order.items

        if not items:
            raise HTTPException(status_code=400, detail="Order must contain at least one item.")

        for item in items:
            if not item.productId or not isinstance(item.qty, int) or item.qty <= 0:
                raise HTTPException(status_code=400, detail="Invalid item data: productId and qty required.")

        result = orders_col.insert_one(order.dict())
        return {"id": str(result.inserted_id)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Order creation failed: {str(e)}")


#GET /orders/{user_id}
def get_orders_by_user(user_id: str, limit: int = 10, offset: int = 0) -> Dict[str, Any]:
    try:
        orders_cursor = (
            orders_col.find({"userId": user_id})
            .sort("_id", 1)
            .skip(offset)
            .limit(limit)
        )

        data: List[Dict[str, Any]] = []

        for order in orders_cursor:
            total = 0.0
            enriched_items = []

            for item in order.get("items", []):
                product_id = item.get("productId")
                qty = item.get("qty", 0)

                if not is_valid_objectid(product_id):
                    product = None
                else:
                    product = products_col.find_one({"_id": ObjectId(product_id)})

                product_detail = {
                    "name": product["name"] if product else "Unknown Product",
                    "id": str(product["_id"]) if product else product_id,
                }

                price = product.get("price", 0) if product else 0
                total += qty * price

                enriched_items.append({
                    "productDetail": product_detail,
                    "qty": qty
                })

            data.append({
                "id": str(order["_id"]),
                "items": enriched_items,
                "total": round(total, 2)
            })

        return {
            "data": data,
            "page": {
                "next": offset + limit,
                "limit": len(data),
                "previous": max(0, offset - limit)
            }
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve orders: {str(e)}")
