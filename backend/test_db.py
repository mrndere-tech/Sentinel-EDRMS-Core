from db import get_connection

conn = get_connection()
print("Connection successful:", conn)
conn.close()
