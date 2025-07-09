from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    year: int
    description: str
    
class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    class Config:
        # orm_mode = True
        from_attributes = True