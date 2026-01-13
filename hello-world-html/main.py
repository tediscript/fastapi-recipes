from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Returns a rendered HTML page with a Hello World message.
    
    This example demonstrates:
    - Server-side rendering using Jinja2Templates
    - Request object for template context
    - HTMLResponse for returning HTML content
    """
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "message": "Hello World!"}
    )


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
