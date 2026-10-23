
from pydantic import BaseModel, ConfigDict


class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int = 0


class ProductResponse(ProductCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
