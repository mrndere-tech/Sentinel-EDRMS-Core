CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    FOREIGN KEY (role_id) REFERENCES Roles(role_id) 
);
CREATE TABLE Documents (
    document_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    file_path TEXT NOT NULL,
    file_type VARCHAR(50),
    uploaded_by INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (uploaded_by) REFERENCES Users(user_id)
);
CREATE TABLE AuditLogs (
    log_id SERIAL PRIMARY KEY,
    user_id INTEGER,
    action VARCHAR(100) NOT NULL,
    document_id INTEGER,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (document_id) REFERENCES Documents(document_id)
);
CREATE TABLE Roles (
    role_id SERIAL PRIMARY KEY,
    role_name VARCHAR(50) NOT NULL UNIQUE
);
CREATE TABLE DocumentPermissions (
    permission_id SERIAL PRIMARY KEY,
    document_id INTEGER,
    user_id INTEGER,
    permission_type VARCHAR(20),

    FOREIGN KEY (document_id) REFERENCES Documents(document_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
