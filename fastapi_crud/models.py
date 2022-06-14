from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base

class Category(Base):       #Класс таблицы категории
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)

    books = relationship('Book', secondary='bookcategories', back_populates='categories')

class Book(Base):       #Класс таблицы книги
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    isbn = Column(String(20))
    pageCount = Column(Integer)
    shortDescription = Column(String(255))
    longDescription = Column(String(3000))
    publishedDate = Column(DateTime)
    
    categories = relationship('Category', secondary='bookcategories', back_populates='books')
    
    
class BookCategory(Base):       #Класс таблицы для связи книги с категорией
    __tablename__ = "bookcategories"
    id = Column(Integer, primary_key=True, index=True)
    BookId = Column(Integer, ForeignKey('books.id'))
    CategoryId = Column(Integer, ForeignKey('categories.id'))
    

