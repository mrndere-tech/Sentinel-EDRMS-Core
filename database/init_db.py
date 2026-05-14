from backend.db_connection import execute_query


create_users_table = """
CREATE TABLE IF NOT EXISTS Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL UNIQUE,
    PasswordHash TEXT NOT NULL,
    Role TEXT NOT NULL
);
"""


create_documents_table = """
CREATE TABLE IF NOT EXISTS Documents (
    DocumentID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    FilePath TEXT NOT NULL,
    UploadedBy INTEGER,
    DateUploaded TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UploadedBy) REFERENCES Users(UserID)
);
"""


create_auditlogs_table = """
CREATE TABLE IF NOT EXISTS AuditLogs (
    LogID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER,
    Action TEXT NOT NULL,
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);
"""


def initialize_database():
    execute_query(create_users_table)
    execute_query(create_documents_table)
    execute_query(create_auditlogs_table)

    print("Database initialized successfully")


if __name__ == "__main__":
    initialize_database()
