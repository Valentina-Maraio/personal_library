import pandas as pd

def calculate_stats(df):
    
    stats: {}
    
    stats["total_books"] = len(df)
    stats["avg_rating"] = round(df["rating"].mean(),2)
    stats["avg_pages"] = int(df["pages"].mean())
    stats["median_pages"] = int(df["pages"].median())
    stats["std_pages"] = round(df["pages"].std(),2)
    stats["books_per_year"] = (df.groupby("year").size().to_dict())
    stats["top_authors"] = (df["author"].value_counts().head(10).to_dict())
    stats["rating_distribution"] = (df["rating"].round().value_counts().to_dict())
    stats["longest_book"] = (df.loc[df["pages"].idxmax()].to_dict())
    
    return stats
    
    