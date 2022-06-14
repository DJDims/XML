from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models
import schemas

def get_category_by_id(db: Session, category_id: int):
    return db.query(models.Category).get(category_id)

def get_categories(db:Session):
    return db.query(models.Category).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).get(book_id)

def get_book_by_title(db: Session, title: str):
    return db.query(models.Book).filter(models.Book.title == title).first()

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

def create_category(db: Session, category: schemas.Category):
    print(category.name)
    new_category = models.Category(name = category.name)
    db.add(new_category)
    db.commit()
    return new_category
#------------------------------------------------------------------------------------------------------------
def delete_category_by_id(db: Session, id):
    try:
        db.delete(get_category_by_id(db, id))
        db.commit()
        return True
    except:
        return False
    
def delete_book_by_title(db: Session, title):
    try:
        db.delete(get_book_by_title(db, title))
        db.commit()
        return True
    except:
        return False