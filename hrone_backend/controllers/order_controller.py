from fastapi import HTTPException
from hrone_backend.db import connect_db
from bson import ObjectId
from hrone_backend.models.order_model import OrderIn  # Ensure you import your Pydantic model

db = connect_db()
orders_col = db["orders"]
products_col = db["products"]

# ✅ Helper: Validate ObjectId
def is_valid_objectid(id_str: str) -> bool:
    try:
        ObjectId(id_str)
        return True
    except Exception:
        return False

# ✅ POST /orders
def create_order(order: OrderIn):
    try:
        user_id = order.userId
        items = order.items

        # Validate items
        if not items:
            raise HTTPException(status_code=400, detail="Order must contain at least one item.")

        for item in items:
            if not item.productId or not isinstance(item.qty, int) or item.qty <= 0:
                raise HTTPException(status_code=400, detail="Invalid item data: productId and qty required.")

        # Insert into MongoDB
        result = orders_col.insert_one(order.dict())
        return {"id": str(result.inserted_id)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Order creation failed: {str(e)}")

# ✅ GET /orders/{user_id}
def get_orders_by_user(user_id: str, limit: int = 10, offset: int = 0):
    try:
        orders_cursor = orders_col.find({"userId": user_id}).sort("_id", 1).skip(offset).limit(limit)
        data = []

        for order in orders_cursor:
            total = 0
            enriched_items = []

            for item in order.get("items", []):
                product_id = item.get("productId")
                qty = item.get("qty", 0)
                product = None

                if is_valid_objectid(product_id):
                    product = products_col.find_one({"_id": ObjectId(product_id)})

                product_name = product["name"] if product else "Unknown Product"
                product_price = product.get("price", 0) if product else 0

                total += product_price * qty

                enriched_items.append({
                    "productDetail": {
                        "name": product_name,
                        "id": str(product["_id"]) if product else product_id
                    },
                    "qty": qty
                })

            data.append({
                "id": str(order["_id"]),
                "items": enriched_items,
                "total": total
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
