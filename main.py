from fastapi import FastAPI
from routes.todo import todo_router

app = FastAPI()

app.include_router(todo_router, prefix="/api/v1")

