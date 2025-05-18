from src.ingest import load_csv, save_as_parquet
from src.preprocess import preprocess_data
from src.transform import transform_data

raw_path = "data/raw/netflix_titles.csv"
processed_path = "data/processed/netflix_titles.parquet"

df = load_csv(raw_path)
df = preprocess_data(df)
df = transform_data(df)
save_as_parquet(df, processed_path)