import snowflake.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

print("🔍 Loaded ENV values:")
print("User:", os.getenv("SNOWFLAKE_USER"))
print("Password:", os.getenv("SNOWFLAKE_PASSWORD"))
print("Account:", os.getenv("SNOWFLAKE_ACCOUNT"))
print("Warehouse:", os.getenv("SNOWFLAKE_WAREHOUSE"))
print("Database:", os.getenv("SNOWFLAKE_DATABASE"))
print("Schema:", os.getenv("SNOWFLAKE_SCHEMA"))


try:
    # Connect to Snowflake
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )

    # Run test query
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
