import pandas as pd
from snowflake.connector.pandas_tools import write_pandas
from etl.snowflake_connection import get_snowflake_connection

def clean_data(csv_path):
    df = pd.read_csv(csv_path)
    
    # Clean column names: remove whitespace, lowercase, and replace spaces with underscores
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Drop rows missing key values
    df.dropna(subset=["title", "release_year"], inplace=True)

    # Ensure release_year is integer
    df["release_year"] = pd.to_numeric(df["release_year"], errors="coerce")
    df.dropna(subset=["release_year"], inplace=True)
    df["release_year"] = df["release_year"].astype(int)

    return df

def load_to_snowflake(df, table_name):
    conn = get_snowflake_connection()

    # Snowflake prefers uppercase column names if not quoted
    df.columns = [col.upper() for col in df.columns]

    success, nchunks, nrows, _ = write_pandas(conn, df, table_name.upper())
    print(f"✅ Uploaded {nrows} rows to table {table_name.upper()}")
    
    conn.close()

def main():
    file_path = "M:/MAJORPROJECTS/Netflix_Data_Warehouse_Project/data/netflix_titles_sample.csv"
    df_clean = clean_data(file_path)
    load_to_snowflake(df_clean, "raw_titles")

if __name__ == "__main__":
    main()
