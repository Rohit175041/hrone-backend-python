from fastapi import HTTPException
from hrone_backend.db import connect_db
from bson import ObjectId
from hrone_backend.logger import logger

db = connect_db()
products_col = db["products"]

# Create Product
def create_product(product: dict):
    try:
        result = products_col.insert_one(product)
        logger.info(f"Product created with ID: {result.inserted_id}")
        return {"id": str(result.inserted_id)}
    except Exception as e:
        logger.error(f"Failed to create product: {e}")
        raise HTTPException(status_code=400, detail=str(e))


# List Products with Filters and Pagination
def list_products(name=None, size=None, limit=10, offset=0):
    try:
        query = {}
        if name:
            query["name"] = {"$regex": name, "$options": "i"}
        if size:
            query["sizes.size"] = size
            
        logger.info(f"Listing products with query: {query}, limit: {limit}, offset: {offset}")
        products_cursor = products_col.find(query).skip(offset).limit(limit)
        products = [
            {
                "id": str(product["_id"]),
                "name": product["name"],
                "price": product["price"]
            }
            for product in products_cursor
        ]
        logger.info(f"Retrieved {len(products)} product(s)")
        return {
            "data": products,
            "page": {
                "next": offset + limit,
                "limit": len(products),
                "previous": max(0, offset - limit)
            }
        }
    except Exception as e:
        logger.error(f"Failed to list products: {e}")
        raise HTTPException(status_code=500, detail=str(e))
