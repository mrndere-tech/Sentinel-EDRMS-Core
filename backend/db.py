from .db_connection import get_connection


def execute_query(query, parameters=()):
    """Execute a query and return the resulting rows."""
    connection = get_connection()

    try:
        cursor = connection.execute(query, parameters)
        rows = cursor.fetchall()
        connection.commit()
        return rows
    finally:
        connection.close()


def execute_command(query, parameters=()):
    """Execute an INSERT, UPDATE, or DELETE command."""
    connection = get_connection()

    try:
        cursor = connection.execute(query, parameters)
        connection.commit()
        return cursor.lastrowid
    finally:
        connection.close()
