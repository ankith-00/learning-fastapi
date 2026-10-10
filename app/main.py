from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    product_id: int
    product_name: str
    qty: int    



# - - - - - - - - - - - - - QUERY PARAMETERS  (these routes should be above path parameter routes)
@app.get("/products")
def get_product_details(product_name:str, qty:int):
    return {"product_name": f"{product_name}", "qty": qty}




# - - - - - - - - - - - - - PATH PARAMETERS 
@app.get('/{user_name}')
def greet_user(user_name:str):
    return {"message": f"Hello {user_name}, How you doing?"}



# - - - - - - - - - - - - - REQUEST BODY
@app.post("/product_info")
def get_product_info(product: Product):

    return {
        "message": "Product created successfully ",
        "id": product.product_id,
        "name": product.product_name,
        "qty": product.qty
    }