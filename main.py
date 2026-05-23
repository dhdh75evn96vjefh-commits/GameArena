from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
user_data = {"points": 500}

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/join-tournament")
async def join_tournament():
    if user_data["points"] >= 150:
        user_data["points"] -= 150
        return {"status": "success", "remaining_points": user_data["points"]}
    return {"status": "error", "message": "الرصيد غير كافٍ"}
