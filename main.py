from fastapi import FastAPI, Depends, HTTPException
import services, models, schemas
from sqlalchemy.orm import Session
from db import get_db, engine

app = FastAPI()

@app.get("/books", response_model=list[schemas.Book])
def get_all_books(db: Session = Depends(get_db)):
    books = services.get_books(db)
    return books

@app.get("/books/{book_id}", response_model=schemas.Book)
def get_book_by_id(book_id:int, db: Session = Depends(get_db)):
    book = services.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books", response_model=schemas.Book)
def create_new_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return services.create_book(db, book)
    # try:
    #     new_book = services.create_book(db, book)
    #     return new_book
    # except Exception as e:
    #     raise HTTPException(status_code=400, detail=str(e))
    
@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book : schemas.BookCreate, book_id: int, db: Session = Depends(get_db)):
    db_update_book = services.update_book(db, book_id, book)
    if not db_update_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_update_book
    
@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id:int, db: Session = Depends(get_db)):
    db_delete_book = services.delete_book(db, book_id)
    if not db_delete_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_delete_book


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)