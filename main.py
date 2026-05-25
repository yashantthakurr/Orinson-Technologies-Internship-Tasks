
from fastapi import FastAPI
from routers import tasks

app = FastAPI(title="Notes API")

@app.get('/')
def read_root():
    return {"message": "Welcome to Tasks Manager API"}

app.include_router(tasks.router)
