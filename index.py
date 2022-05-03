from fastapi import FastAPI
from fastapi import FastAPI
from routes.books import books_router

app = FastAPI()
app.include_router(books_router)