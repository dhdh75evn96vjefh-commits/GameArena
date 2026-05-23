from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# دالة ذكية لفتح الصفحات
def get_html(filename):
    with open(f"{filename}.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.get("/")
async def home(): return get_html("index")
@app.get("/location")
async def location(): return get_html("location")
@app.get("/withdraw")
async def withdraw(): return get_html("withdraw")
@app.get("/support")
async def support(): return get_html("support")
    
