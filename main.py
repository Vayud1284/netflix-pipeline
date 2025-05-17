# main.py

from src.ingest import load_csv, save_as_parquet

raw_path = "data/raw/netflix_titles.csv"
processed_path = "data/processed/netflix_titles.parquet"

df = load_csv(raw_path)
save_as_parquet(df, processed_path)
