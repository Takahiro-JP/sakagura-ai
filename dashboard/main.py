import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from database import get_all_products, get_post_history, add_product

from fastapi import Form
from fastapi.responses import RedirectResponse
from rag.url_loader import load_url

app = FastAPI()
templates = Jinja2Templates(directory="dashboard/templates")

@app.get("/products/new", response_class=HTMLResponse)
async def new_product(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="product_form.html",
        context={}
    )

@app.post("/products/new")
async def create_product(
    name: str = Form(...),
    series: str = Form(...),
    seimaibuai: int = Form(...),
    price: float = Form(...),
    flavor_notes: str = Form(...),
    target_age: str = Form(...)
):
    add_product(name, series, seimaibuai, price, flavor_notes, target_age)
    return RedirectResponse(url="/", status_code=303)

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

@app.get("/rag", response_class=HTMLResponse)
async def rag_status(request: Request):
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from rag.retriever import collection
    results = collection.get()
    docs = []
    for i, doc_id in enumerate(results["ids"]):
        docs.append({
            "id": doc_id,
            "type": results["metadatas"][i].get("type", ""),
            "source": results["metadatas"][i].get("source", ""),
            "preview": results["documents"][i][:100] + "..."
        })
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"rag_docs": docs}
    )

@app.get("/rag/register", response_class=HTMLResponse)
async def rag_register_form(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="rag_form.html",
        context={}
    )

@app.post("/rag/register", response_class=HTMLResponse)
async def rag_register(request: Request, url: str = Form(...)):
    try:
        preview = load_url(url)
        return templates.TemplateResponse(
            request=request,
            name="rag_form.html",
            context={
                "message": f"登録完了！\n{preview}",
                "message_type": "success"
            }
        )
    except Exception as e:
        return templates.TemplateResponse(
            request=request,
            name="rag_form.html",
            context={
                "message": f"エラー: {e}",
                "message_type": "error"
            }
        )
