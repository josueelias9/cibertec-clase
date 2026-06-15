from pydantic import BaseModel

class ItemPublic(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    id: int

class ItemsPublic(BaseModel):
    items: list[ItemPublic]