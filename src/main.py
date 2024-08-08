from fastapi import FastAPI
from modules.router import all_router

app = FastAPI(title="FastAPI Demo", version="1.0.0")

app.include_router(all_router)
