# src/ingest.py

import pandas as pd
import os
import logging
def load_csv(input_path: str) -> pd.DataFrame:

    logging.info(f"Loading data from {input_path}")

    """Load the raw Netflix dataset from CSV."""
    if not os.path.exists(input_path):

        logging.error(f"File not found: {input_path}")
        raise FileNotFoundError(f"File not found: {input_path}")
    df = pd.read_csv(input_path)
    print(f"Loaded data shape: {df.shape}")
    logging.info(f"Loaded data shape: {df.shape}")
    return df

def save_as_parquet(df: pd.DataFrame, output_path: str):

    logging.info(f"Saving data to {output_path}")

    """Save the DataFrame to a Parquet file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_parquet(output_path, index=False)
    print(f"Saved Parquet file to: {output_path}")
    logging.info("Save successful.")
