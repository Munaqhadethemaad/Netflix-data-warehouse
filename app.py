import streamlit as st
import pandas as pd
import snowflake.connector

# Function to get data from Snowflake
def fetch_data():
    conn = snowflake.connector.connect(
    user='munaqhad',
    password='Ethmaad07865525',
    account='CKUXZUS-QR39133',  # Replace with your full Snowflake account identifier
    warehouse='COMPUTE_WH',
    database='NETFLIX_DB',
    schema='PUBLIC'
)

    
    query = """
        SELECT DT.TITLE, FR.RELEASE_DATE, FR.VIEW_COUNT
        FROM FACT_TITLE_RELEASE FR
        JOIN DIM_TITLE DT ON FR.TITLE_ID = DT.TITLE_ID
        WHERE EXTRACT(YEAR FROM FR.RELEASE_DATE) BETWEEN 2010 AND 2020
        ORDER BY FR.VIEW_COUNT DESC
    """
    
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Streamlit UI
st.title("📊 Netflix Titles Dashboard")
st.subheader("Top Viewed Titles (2010–2020)")

df = fetch_data()

if not df.empty:
    st.dataframe(df)

    st.bar_chart(df.head(10).set_index('TITLE')["VIEW_COUNT"])

    df['Year'] = pd.to_datetime(df['RELEASE_DATE']).dt.year
    st.line_chart(df.groupby('Year')["VIEW_COUNT"].sum())

else:
    st.warning("No data found for the selected period.")
