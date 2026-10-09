from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id:int
    name:str
    email:str


user_data = [
    {
        "id": 1,
        "name": "Rajeev",
        "age": 20,
        "email": "rajeev@gmail.com",
        "city": "Bengaluru"
    }
]


@app.get('/', response_model=User)
def root():
    return user_data[0]