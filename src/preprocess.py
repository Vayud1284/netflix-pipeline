import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and preprocess the Netflix dataset."""

    # Drop rows with missing titles or types
    df = df.dropna(subset=["title", "type"])  #s8 US  s13 germany
    df = df.drop_duplicates()

    # Strip leading/trailing whitespace from all string columns
    str_cols = df.select_dtypes(include='object').columns
    df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())

    # Convert 'date_added' to datetime
    if 'date_added' in df.columns:
        df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

    # Standardize column names (lowercase, underscores)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    return df