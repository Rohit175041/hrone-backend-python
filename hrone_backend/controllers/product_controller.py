from fastapi import HTTPException
from hrone_backend.db import connect_db
from bson import ObjectId

db = connect_db()
products_col = db["products"]

# Create Product
def create_product(product: dict):
    try:
        result = products_col.insert_one(product)
        return {"id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# List Products with Filters and Pagination
def list_products(name=None, size=None, limit=10, offset=0):
    try:
        query = {}
        if name:
            query["name"] = {"$regex": name, "$options": "i"}
        if size:
            query["sizes.size"] = size

        products_cursor = products_col.find(query).skip(offset).limit(limit)
        products = [
            {
                "id": str(product["_id"]),
                "name": product["name"],
                "price": product["price"]
            }
            for product in products_cursor
        ]

        return {
            "data": products,
            "page": {
                "next": offset + limit,
                "limit": len(products),
                "previous": max(0, offset - limit)
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
