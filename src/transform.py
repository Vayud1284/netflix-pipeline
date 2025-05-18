import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Perform feature transformations on the Netflix dataset."""

    # Extract year from 'date_added' column
    if 'date_added' in df.columns:
        df['year_added'] = df['date_added'].dt.year

    # Extract first country if multiple are listed
    if 'country' in df.columns:
        df['main_country'] = df['country'].fillna("Unknown").apply(lambda x: x.split(",")[0])

    # Convert 'duration' to numeric (minutes or seasons)
    if 'duration' in df.columns:
        df['duration_num'] = df['duration'].str.extract(r'(\d+)').astype(float)
        df['duration_type'] = df['duration'].str.extract(r'([a-zA-Z]+)').fillna('')

    return df