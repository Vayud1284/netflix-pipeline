# src/ingest.py

import pandas as pd
import os

def load_csv(input_path: str) -> pd.DataFrame:
    """Load the raw Netflix dataset from CSV."""
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"File not found: {input_path}")
    df = pd.read_csv(input_path)
    print(f"Loaded data shape: {df.shape}")
    return df

def save_as_parquet(df: pd.DataFrame, output_path: str):
    """Save the DataFrame to a Parquet file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_parquet(output_path, index=False)
    print(f"Saved Parquet file to: {output_path}")
