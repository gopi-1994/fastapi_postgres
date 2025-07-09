from models import Book
from schemas import BookCreate
from sqlalchemy.orm import Session

def create_book(db:Session, data: BookCreate):
    book_instance = Book(**data.dict())
    db.add(book_instance)
    db.commit()
    db.refresh(book_instance)
    return book_instance

def get_books(db: Session):
    return db.query(Book).all()
    