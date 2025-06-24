Netflix Data Warehouse Dashboard

A Streamlit-powered analytics dashboard that connects to a Snowflake data warehouse and visualizes Netflix title data from 2010 to 2020.


Tech Stack

- **Streamlit** — for building the dashboard
- **Snowflake** — as the cloud data warehouse
- **Python** — main programming language
- **Pandas** — data manipulation
- **dotenv** — secure credential management

Features

Connects securely to Snowflake using Python


Displays top viewed Netflix titles (2010–2020)


Yearly trend visualization (line chart)


Interactive bar chart of most popular titles


Project Structure

├── app.py                             # Streamlit dashboard app

├── test_connection.py                 # Test Snowflake DB connection

├── requirements.txt                   # Dependencies

├── .gitignore                         # Prevents secrets from being tracked

└── .env                               # Not tracked – contains credentials



Step-by-Step: 

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

## How to Run the Project

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/netflix-data-warehouse.git
cd netflix-data-warehouse

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

2. Install Dependencies

pip install -r requirements.txt


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

3 Setup Snowflake

Create a database, warehouse, schema manually or via sql/create_tables.sql

Update your credentials in .env or config.py

#######################################################

4. Run ETL Script

python etl/clean_and_load.py

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

5. Run the Streamlit App

streamlit run streamlit_app/app.py

