from pydantic import BaseModel

class BookCreate(BaseModel):
    
    title: str
    author: str
    year: int
    pages: int
    rating: float
    shelf: str
    
class Book(BookCreate):
    
    id: int
    cover_url: str
    
    class Config:
        from_attributes: True