from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load CSV
df = pd.read_csv("goodreads_library_export.csv")

# Clean numeric columns
df["Year Published"] = pd.to_numeric(df["Year Published"], errors="coerce")
df["Average Rating"] = pd.to_numeric(df["Average Rating"], errors="coerce")
df["Number of Pages"] = pd.to_numeric(df["Number of Pages"], errors="coerce")

@app.get("/")
def home():
    return {"status": "Backend running"}

@app.get("/summary")
def summary():
    
    return {
        "total_books": len(df),
        "read books": len(df[df["Exclusive Shelf"]=="read"]),
        "avg_rating": round(df["Average Rating"].mean(),2),
        "avg_pages": int(df["Number of Pages"].mean())
    }

@app.get("/books_per_year")
def books_per_year():
    
    data = (
        df.groupby("Year Published")
        .size()
        .reset_index(name="count")
        .dropna()        
    )
    
    return data.to_dict(orient="records")

@app.get("/top_authors")
def top_authors():
    
    data = (
        df["Author"]
        .value_counts()
        .head(10)
        .reset_index()
    )
    
    data.columns=["author","count"]
    
    return data.to_dict(orient="records")

