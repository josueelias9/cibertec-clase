from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    id: int = None


class Items(BaseModel):
    items: list[Item]