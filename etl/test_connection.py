import snowflake.connector
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

try:
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )

    cursor = conn.cursor()
    cursor.execute("SELECT CURRENT_USER(), CURRENT_ROLE(), CURRENT_DATABASE();")
    for row in cursor:
        print("✅ Connected to Snowflake!")
        print(f"User: {row[0]}, Role: {row[1]}, Database: {row[2]}")
    cursor.close()
    conn.close()

except Exception as e:
    print("❌ Snowflake connection failed:")
    print(e)
