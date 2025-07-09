from models import Book
from schemas import BookCreate
from sqlalchemy.orm import Session

def create_book(db:Session, data: BookCreate):
    book_instance = Book(**data.model_dump())
    db.add(book_instance)
    db.commit()
    db.refresh(book_instance)
    return book_instance

def get_books(db: Session):
    return db.query(Book).all()
    
def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def update_book(db: Session, book_id: int, data: BookCreate):
    book_queryset = db.query(Book).filter(Book.id == book_id).first()
    if not book_queryset:
        return None
    for key, value in data.model_dump().items():
        setattr(book_queryset, key, value)
    db.commit()
    db.refresh(book_queryset)
    return book_queryset

def delete_book(db: Session, book_id: int):
    book_queryset = db.query(Book).filter(Book.id == book_id).first()
    if not book_queryset:
        return None
    db.delete(book_queryset)
    db.commit()
    return book_queryset