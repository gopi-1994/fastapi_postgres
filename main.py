from fastapi import FastAPI, Depends, HTTPException
import services, models, schemas
from sqlalchemy.orm import Session
from db import get_db, engine

app = FastAPI()

@app.get("/books", response_model=list[schemas.Book])
def get_all_books(db: Session = Depends(get_db)):
    books = services.get_books(db)
    return books

@app.post("/books", response_model=schemas.Book)
def create_new_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return services.create_book(db, book)
    # try:
    #     new_book = services.create_book(db, book)
    #     return new_book
    # except Exception as e:
    #     raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)