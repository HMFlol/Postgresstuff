import psycopg2
import os
import time

host = os.environ['PG_HOST']
user = os.environ['PG_USER']
password = os.environ['PG_PASSWORD']
database = os.environ['PG_DB']

# Retry connection for a certain number of times
max_retries = 10
retry_interval = 5

for retry in range(max_retries):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            dbname=database
        )
        print("Connected to PostgreSQL")
        break
    except Exception as e:
        print(f"Attempt {retry + 1}/{max_retries}: Error connecting to database - {e}")
        time.sleep(retry_interval)
else:
    print("Max retries reached. Could not connect to the database.")

# Create a new table
table_name = "rynes_stuff"
create_table_query = f"""
    CREATE TABLE {table_name} (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255)
    )
"""

try:
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)
        print(f"Created '{table_name}' table")
except Exception as e:
    print(f"Error creating table: {e}")

# Close the connection
if connection:
    connection.close()
    print("Connection closed")

