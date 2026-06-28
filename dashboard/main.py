import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from database import get_all_products, get_post_history

app = FastAPI()
templates = Jinja2Templates(directory="dashboard/templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    products = get_all_products()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"products": products}
    )

@app.get("/history", response_class=HTMLResponse)
async def history(request: Request):
    posts = get_post_history()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"posts": posts}
    )