from fastapi import FastAPI
import yaml
from fastapi.responses import PlainTextResponse, HTMLResponse, JSONResponse

from routes import items, others,websocket

app = FastAPI(
    title="Clase 3.2 Cibertec",
    description="Ejemplo de FastAPI con OpenAPI en YAML",
    version="6.6.6"
)

app.include_router(items.router)
app.include_router(websocket.router)
# app.include_router(others.router)

# endpoint para mostrar el OpenAPI en formato YAML

@app.get("/openapi")
def openapi_yaml():
    yaml_content = yaml.dump(app.openapi())
    return PlainTextResponse(content=yaml_content, media_type="text/yaml")    


# endpoints para mostrar el uso de schemas


