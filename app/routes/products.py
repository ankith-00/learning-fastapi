from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


# PRODUCTS DATA
products_data = {
    1:{
        "id": 1,
        "product_name": "codex",
        "mrp": 499
    },
    2:{
        "id":2,
        "product_name": "claude",
        "mrp": 999
    }
}



@router.get('/')
def get_all_products():
    return {"data": products_data}


@router.get('/{product_id}')
def get_product(product_id:int):
    if product_id in products_data:
        return products_data[product_id]
    else:
        return {"message": "Product not found"}
