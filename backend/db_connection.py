import sqlite3
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Central database location
DATABASE_DIR = BASE_DIR / "database"
DATABASE_DIR.mkdir(exist_ok=True)

DATABASE_PATH = DATABASE_DIR / "sentinel_edrms.db"


def get_connection():
    """Create and return a connection to the Sentinel EDRMS database."""
    connection = sqlite3.connect(DATABASE_PATH)

    # Return rows that can be accessed by column name
    connection.row_factory = sqlite3.Row

    # Enforce foreign-key relationships
    connection.execute("PRAGMA foreign_keys = ON")

    return connection
