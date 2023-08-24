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

# Close the connection
if connection:
    connection.close()
    print("Connection closed")

