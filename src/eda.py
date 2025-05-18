import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda(parquet_path: str):
    # Load processed data
    df = pd.read_parquet(parquet_path)

    print("\n--- Dataset Overview ---")
    print(df.info())

    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    print("\n--- Top 5 Content Types ---")
    print(df['type'].value_counts())

    print("\n--- Top 10 Countries ---")
    print(df['main_country'].value_counts().head(10))

    print("\n--- Content Over Years ---")
    if 'date_added' in df.columns:
        df['year_added'] = df['date_added'].dt.year
        print(df['year_added'].value_counts().sort_index())

        # Plot content count over time
        plt.figure(figsize=(10, 5))
        sns.countplot(data=df, x='year_added', order=sorted(df['year_added'].dropna().unique()))
        plt.xticks(rotation=45)
        plt.title("Content Added to Netflix Over Time")
        plt.tight_layout()
        plt.show()

    # Plot content type
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='type')
    plt.title("Content Type Distribution")
    plt.show()

    # Plot top countries
    plt.figure(figsize=(10, 4))
    top_countries = df['main_country'].value_counts().head(10)
    sns.barplot(x=top_countries.index, y=top_countries.values)
    plt.title("Top 10 Countries Producing Netflix Content")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Duration distribution
    if 'duration_num' in df.columns and 'duration_type' in df.columns:
        plt.figure(figsize=(8, 5))
        sns.histplot(data=df, x='duration_num', hue='duration_type', bins=30, kde=True)
        plt.title("Content Duration Distribution")
        plt.show()