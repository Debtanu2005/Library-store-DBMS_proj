import psycopg2
import os
# from src.logger import logging
from src.exception import MyException
import sys
import dotenv
dotenv.load_dotenv()

database_url = os.getenv("DATABASE_URL")
print(f"Database URL: {database_url}")  # Debugging line to check if DATABASE_URL is loaded
conn = None

def connect_db() -> psycopg2.extensions.connection:
    global conn

    if conn is not None and conn.closed == 0:
        print("Database already connected.")
        return conn

    try:
        DATABASE_URL = os.getenv("DATABASE_URL")

        if not DATABASE_URL:
            raise Exception("DATABASE_URL not found in environment variables")

        conn = psycopg2.connect(DATABASE_URL)

        print("Database connection established successfully.")
        return conn

    except Exception as e:
        raise MyException(e, sys)


def disconnect_db():
    global conn

    if conn is None or conn.closed != 0:
        return None

    try:
        conn.close()
        print("Database connection closed successfully.")
        return None

    except Exception as e:
        raise MyException(e, sys)