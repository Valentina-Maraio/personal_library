from fastapi import FastAPI, Depends
import pandas as pd
from database import SessionLocal, engine
from models import Book
from schemas import BookCreate
from stats import calculate_stats
from database import Base
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencies
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

# Load books as dataframe
def get_df(db: any):

    books = db.query(Book).all()
    data = []
    for b in books:
        data.append({
            "title": b.title,
            "author": b.author,
            "year": b.year,
            "rating": b.rating,
            "shelf": b.shelf
        })

    return pd.DataFrame(data)

# Cover fetch
def get_cover(title: str):

    return f"https://covers.openlibrary.org/b/title/{title}L.jpg"

# Add new book


@app.post("/books")
def add_book(book: BookCreate, db: Session = Depends(get_db)):

    cover = get_cover(book.title)

    new_book = Book(
        title=book.title,
        author=book.author,
        year=book.year,
        pages=book.pages,
        rating=book.rating,
        shelf=book.shelf,
        cover_url=cover
    )

    db.add(new_book)
    db.commit()

    return {"status": "added"}

# Get books
@app.get("/books")
def get_books(db: Session = Depends(get_db)):
    
    return db.query(Book).all()

# Statistics endpoint
@app.get("/stats")
def stats(db: Session = Depends(get_db)):
    
    df = get_df(db)
    
    return calculate_stats(df)