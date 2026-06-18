
from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter(prefix="/items")

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    id: int = None


class Items(BaseModel):
    items: list[Item]

items = [
    Item(id=1 , name="Foo", description="A very nice Item", price=35.4, tax=3.2),
    Item(id=2 , name="Bar", description="The best Item", price=23.4, tax=0.8),
    Item(id=3 , name="Baz", description="The worst Item", price=5.4, tax=1.2),
]




@router.get("/{id}", response_model=Item)
def read_item(id:int):
    """Este endpoint devuelve un item por su id"""
    item = next((item for item in items if item.id == id), None)
    if item is None:
        return Item(id=id, name="Unknown", description="No description", price=0.0, tax=0.0)
    return item


@router.get("/", response_model=Items)
def read_items():
    """Este endpoint devuelve todos los items"""
    return Items(items=items)



@router.post("/")
def create_item(item: Item):
    """
    Este endpoint recibe un objeto Item en el cuerpo de la solicitud y devuelve un mensaje de éxito. El modelo Item se define utilizando Pydantic, lo que permite validar los datos de entrada y generar automáticamente la documentación OpenAPI.
    """
    return {"message": "Item created successfully"}