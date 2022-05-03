import imp
from fastapi import APIRouter
from models.books import Books
from config.database import connection
from schemas.books import booksEntity, listOfBookEntity
from bson import ObjectId

books_router = APIRouter()

@books_router.get('/maailma')
async def hei_maailmaa():
    return "Hei! Maailmaa"

@books_router.get('/books')
async def find_all_books():
    return listOfBookEntity(connection.books.books.find())

@books_router.post('/books')
async def post_book(books: Books):
    connection.books.books.insert_one(dict(books))
    return listOfBookEntity(connection.books.books.find())

@books_router.get('/books/{bookId}')
async def find_book(bookId):
    return booksEntity(connection.books.books.find_one({"_id": ObjectId(bookId)}))

@books_router.put('/books/{bookId}')
async def update_book(bookId, books: Books):
    connection.books.books.find_one_and_update(
        {"_id": ObjectId(bookId)},
        {"$set": dict(books)}
    )
    return booksEntity(connection.books.books.find_one({"_id": ObjectId(bookId)}))


@books_router.delete('/books/{bookId}')
async def delete_book(bookId):
    return booksEntity(connection.books.books.find_one_and_delete({"_id": ObjectId(bookId)}))


