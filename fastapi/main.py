from fastapi import FastAPI
import yaml
from fastapi.responses import PlainTextResponse, HTMLResponse, JSONResponse

app = FastAPI(
    title="Clase 3.2 Cibertec",
    description="Ejemplo de FastAPI con OpenAPI en YAML",
    version="6.6.6"
)

# endpoints para validar el tipo de contenido de la respuesta, y el endpoint para mostrar el OpenAPI en formato YAML

@app.get("/", response_class=JSONResponse)
async def root():
    return {"message": "Hello World"}


@app.get("/html_content", response_class=HTMLResponse)
def html_content():
    html_content = """<!DOCTYPE html>
        <html>
        <head>    <title>HTML Content</title>
        </head>
        <body>
            <h1>This is an HTML response</h1>
            <p>FastAPI can return HTML content as well.</p>
        </body>
        </html>"""
    return html_content


@app.get("/text_content", response_class=PlainTextResponse)
def text_content():
    text_content = "This is a plain text response"
    return text_content

# endpoint para mostrar el OpenAPI en formato YAML

@app.get("/openapi")
def openapi_yaml():
    yaml_content = yaml.dump(app.openapi())
    return PlainTextResponse(content=yaml_content, media_type="text/yaml")    


# endpoints para mostrar el uso de schemas



from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    id: int = None

items = [
    Item(id=1 , name="Foo", description="A very nice Item", price=35.4, tax=3.2),
    Item(id=2 , name="Bar", description="The best Item", price=23.4, tax=0.8),
    Item(id=3 , name="Baz", description="The worst Item", price=5.4, tax=1.2),
]




@app.get("/example/{id}", response_model=Item)
def read_item(id:int):
    """Este endpoint devuelve un item por su id"""
    item = next((item for item in items if item.id == id), None)
    if item is None:
        return Item(id=id, name="Unknown", description="No description", price=0.0, tax=0.0)
    return item


@app.post("/example")
def create_item(item: Item):
    """
    Este endpoint recibe un objeto Item en el cuerpo de la solicitud y devuelve un mensaje de éxito. El modelo Item se define utilizando Pydantic, lo que permite validar los datos de entrada y generar automáticamente la documentación OpenAPI.
    """
    return {"message": "Item created successfully"}