import pandas as pd
from sqlalchemy import create_engine

def load_to_postgres(cleaned_df):
    """
    Load cleaned data into a PostgreSQL database.

    Parameters:
        cleaned_df (DataFrame): Cleaned e-commerce data.
    """
    # Database connection
    engine = create_engine('postgresql://postgres:122313@localhost:5432/ecommerce_db')

    # Create table if not exists (for fresh table)
    cleaned_df.head(0).to_sql('ecommerce_table', engine, if_exists='replace', index=False)

    # Load in chunks for large datasets
    cleaned_df.to_sql('ecommerce_table', engine, if_exists='append', index=False, chunksize=10000)
    print("Data successfully loaded to PostgreSQL!")

if __name__ == "__main__":
    # Load cleaned data from 'Data/cleaned.csv'
    cleaned_df = pd.read_csv('Data/cleaned.csv')

    # Load data to PostgreSQL
    load_to_postgres(cleaned_df)
