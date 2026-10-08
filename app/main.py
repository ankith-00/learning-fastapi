from fastapi import FastAPI
from routes import users, products

app = FastAPI()
app.include_router(users.router)
app.include_router(products.router)


app.get('/')
def root():
    return {"message":"Hello World !"}
