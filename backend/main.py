# ============================================================
# ЭТО ГЛАВНЫЙ ФАЙЛ ПРИЛОЖЕНИЯ (main.py)
# Он запускает сервер FastAPI и подключает:
#   • HTML‑страницы (templates)
#   • статические файлы (CSS, JS, картинки)
#   • роуты (auth, users, news, training, stats)
# Если приложение не работает — чаще всего проблема здесь.
# ============================================================

import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# 🔥 ВАЖНО: правильный импорт для Render
from backend.routers import auth, users, news, training, stats

app = FastAPI(title="Tennis Web App")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "frontend", "templates"))
STATIC_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "frontend", "static"))

print("BASE_DIR =", BASE_DIR)
print("TEMPLATES_DIR =", TEMPLATES_DIR)
print("STATIC_DIR =", STATIC_DIR)

templates = Jinja2Templates(directory=TEMPLATES_DIR)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(news.router)
app.include_router(training.router)
app.include_router(stats.router)

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )
