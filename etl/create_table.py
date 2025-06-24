from etl.snowflake_connection import get_snowflake_connection

def create_raw_titles_table():
    create_sql = """
    CREATE OR REPLACE TABLE raw_titles (
        show_id STRING,
        type STRING,
        title STRING,
        director STRING,
        cast STRING,
        country STRING,
        date_added STRING,
        release_year INT,
        rating STRING,
        duration STRING,
        listed_in STRING,
        description STRING
    );
    """
    conn = get_snowflake_connection()
    cursor = conn.cursor()
    cursor.execute(create_sql)
    print("✅ Table 'raw_titles' created successfully.")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_raw_titles_table()