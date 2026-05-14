import sqlite3
from sqlite3 import Error

DATABASE_PATH = "../database/sentinel_edrms.db"


def connect_db():
    """
    Creates a connection to the SQLite database
    """
    connection = None

    try:
        connection = sqlite3.connect(DATABASE_PATH)
        print("Database connection successful")

    except Error as e:
        print(f"Database connection failed: {e}")

    return connection


def execute_query(query, parameters=()):
    """
    Executes INSERT, UPDATE, DELETE queries
    """

    connection = connect_db()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute(query, parameters)
        connection.commit()
        print("Query executed successfully")

    except Error as e:
        print(f"Query failed: {e}")

    finally:
        connection.close()


def fetch_query(query, parameters=()):
    """
    Executes SELECT queries
    """

    connection = connect_db()

    if connection is None:
        return []

    cursor = connection.cursor()

    try:
        cursor.execute(query, parameters)
        results = cursor.fetchall()
        return results

    except Error as e:
        print(f"Fetch failed: {e}")
        return []

    finally:
        connection.close()
