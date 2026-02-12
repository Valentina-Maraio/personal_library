from sqlalchemy import Column, Integer, String, Float
from database import Base

class Book(Base):

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    
    title = Column(String)
    author = Column(String)
    year = Column(Integer)
    pages = Column(Integer)
    rating = Column(Float)
    shelf = Column(String)
    cover_url = Column(String)
    
    