from src.ingest import load_csv, save_as_parquet
from src.preprocess import preprocess_data
import os

# File paths
raw_path = os.path.join("data", "raw", "netflix_titles.csv")
processed_path = os.path.join("data", "processed", "netflix_titles.parquet")

# Load raw data
df = load_csv(raw_path)

# Preprocess the data
df_clean = preprocess_data(df)

# Save processed data
save_as_parquet(df_clean, processed_path)
