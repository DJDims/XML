from fastapi import FastAPI
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/categories/")    #посмотреть категории
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)

@app.post("/categories/", response_model=schemas.Category)  #добавить категорию
def add_category(category: schemas.Category, db: Session = Depends(get_db)):
    return crud.create_category(db, category)
#--------------------------------------------------------------------------------
@app.get("/categories/{cat_id}")    #посмотреть категории по ид
def read_categories_by_id(cat_id: int, db: Session = Depends(get_db)):
    return crud.get_category_by_id(db, cat_id)

@app.get("/books/")     #посмотреть все книги
def read_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@app.get("/books/{book_id}")    #посмотреть книгу по номеру
def read_books_by_id(book_id: int, db: Session = Depends(get_db)):
    return crud.get_book_by_id(db, book_id)

@app.get("/books/{book_title}")     #посмотреть книгу по названию
def read_books_by_title(book_title: str, db: Session = Depends(get_db)):
    return crud.get_book_by_title(db, book_title)

@app.delete("/categories/delete/{category_id}")
def delete_category_by_id(category_id: str, db: Session = Depends(get_db)):
    return crud.delete_category_by_id(db, category_id)