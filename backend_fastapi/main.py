import yaml
from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse
from routes import items, others

app = FastAPI(
    title="My FastAPI Application",
    description="This is a sample FastAPI application with multiple routes.",
    version="1.0.0",
    
)


app.include_router(items.router)
app.include_router(others.router)



@app.get("/openapi", include_in_schema=False)
def openapi_yaml():
    yaml_content = yaml.dump(
        app.openapi(),
        sort_keys=False
    )

    return PlainTextResponse(content=yaml_content, media_type="text/yaml")

