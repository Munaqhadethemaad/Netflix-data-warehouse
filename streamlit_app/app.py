import streamlit as st
import pandas as pd
import snowflake.connector
import os
from dotenv import load_dotenv

load_dotenv()

st.title("🎬 Netflix Data Dashboard")

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")
)

# Load data
query = "SELECT * FROM raw_titles LIMIT 1000"
df = pd.read_sql(query, conn)

# Filters
genre_filter = st.selectbox("Select Genre", sorted(set(df['listed_in'].dropna().str.split(', ').sum())))
year_filter = st.slider("Select Release Year", int(df['release_year'].min()), int(df['release_year'].max()))

filtered_df = df[df['listed_in'].str.contains(genre_filter, na=False) & (df['release_year'] == year_filter)]

st.dataframe(filtered_df)

# Chart
st.bar_chart(filtered_df['rating'].value_counts())