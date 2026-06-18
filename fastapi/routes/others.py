
# endpoints para validar el tipo de contenido de la respuesta, y el endpoint para mostrar el OpenAPI en formato YAML
from fastapi.responses import PlainTextResponse, HTMLResponse, JSONResponse

from fastapi import APIRouter

router = APIRouter(prefix="/others")


@router.get("/", response_class=JSONResponse)
async def root():
    return {"message": "Hello World"}


@router.get("/html_content", response_class=HTMLResponse)
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


@router.get("/text_content", response_class=PlainTextResponse)
def text_content():
    text_content = "This is a plain text response"
    return text_content