from fastapi import FastAPI, Security
from fastapi.middleware.cors import CORSMiddleware

from backend.app.endpoints.login_router import login_router

app = FastAPI(
    root_path='/api'
)

app.include_router(login_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Савелий": "Солнечный ребенок"}
