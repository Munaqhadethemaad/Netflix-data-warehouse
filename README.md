Netflix Data Warehouse Dashboard

A Streamlit-powered analytics dashboard that connects to a Snowflake data warehouse and visualizes Netflix title data from 2010 to 2020.


Tech Stack

- **Streamlit** — for building the dashboard
- **Snowflake** — as the cloud data warehouse
- **Python** — main programming language
- **Pandas** — data manipulation
- **dotenv** — secure credential management

Project Structure

├── app.py               # Streamlit dashboard app
├── test_connection.py   # Test Snowflake DB connection
├── requirements.txt     # Dependencies
├── .gitignore           # Prevents secrets from being tracked
└── .env                 # Not tracked – contains credentials
