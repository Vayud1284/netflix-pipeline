from src.ingest import load_csv, save_as_parquet
from src.preprocess import preprocess_data
from src.transform import transform_data
from src.send_email import send_email
from src.eda import run_eda
from src.utils import setup_logging
import logging

setup_logging()

raw_path = "data/raw/netflix_titles.csv"
processed_path = "data/processed/netflix_titles.parquet"
try:
    df = load_csv(raw_path)
    df = preprocess_data(df)
    df = transform_data(df)

    save_as_parquet(df, processed_path)
    run_eda(processed_path)
    send_email("✅ Pipeline Success", f"Successfully processed {len(df)} records.")
except Exception as e:
    logging.error(f"Pipeline failed: {e}")
    # Email failure
    send_email("❌ Pipeline Failed", str(e))
logging.info("Data pipeline finished successfully.")