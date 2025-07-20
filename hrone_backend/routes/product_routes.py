from fastapi import APIRouter, Query
from hrone_backend.controllers.product_controller import create_product, list_products

router = APIRouter()

# POST /products - create a new product
@router.post("/products")
def create_product_route(product: dict):
    return create_product(product)

# GET /products - list products with optional filters
@router.get("/products")
def list_products_route(
    name: str = Query(default=None),
    size: str = Query(default=None),
    limit: int = Query(default=10, ge=0),
    offset: int = Query(default=0, ge=0)
):
    return list_products(name=name, size=size, limit=limit, offset=offset)
