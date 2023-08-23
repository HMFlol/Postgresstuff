import psycopg2
import os

host = os.environ['PG_HOST']
user = os.environ['PG_USER']
password = os.environ['PG_PASSWORD']
database = os.environ['PG_DB']

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=database
    )
    print("Connected to PostgreSQL")
except Exception as e:
    print("Error:", e)
finally:
    if connection:
        connection.close()
        print("Connection closed")
