from fastapi import FastAPI
from app.routes.analyze import router
from fastapi.middleware.cors import CORSMiddleware
from app.routes.chat import router as chat_router
from app.routes.history import (
    router as history_router
)

from app.database import (
    init_db
)

app = FastAPI(title="Vision")
init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(chat_router)
app.include_router(history_router)


@app.get("/")
def root():
    return {
        "message" : "Vision Backend Running"
    }