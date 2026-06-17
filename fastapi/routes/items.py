from fastapi import APIRouter

from models import ItemPublic, ItemsPublic

router = APIRouter(prefix="/items", tags=["items"])

items = [
    ItemPublic(id=1 , name="Foo", description="A very nice Item", price=35.4, tax=3.2),
    ItemPublic(id=2 , name="Bar", description="The best Item", price=23.4, tax=0.8),
    ItemPublic(id=3 , name="Baz", description="The worst Item", price=5.4, tax=1.2),
]

@router.get("/{id}", response_model=ItemPublic)
def read_item(id:int):
    item = next((item for item in items if item.id == id), None)
    if item is None:
        return ItemPublic(id=id, name="Unknown", description=None, price=0.0, tax=None)
    return item


@router.get("/", response_model=ItemsPublic)
def read_items():
    return ItemsPublic(items=items)

@router.post("/")
def create_item(item: ItemPublic)-> ItemPublic:
    """Sirve para crear un item"""
    return item
