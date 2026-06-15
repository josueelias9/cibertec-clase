from fastapi import APIRouter
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse

router = APIRouter(prefix="/others", tags=["others"])


@router.get("/json_content", response_class=JSONResponse)
def json_content():
    return {"Hello": "World"}

@router.get("/html_content", response_class=HTMLResponse)
async def html_content():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@router.get("/text_content", response_class=PlainTextResponse)
def text_content():
    return "Este es un texto plano de ejemplo"

@router.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}