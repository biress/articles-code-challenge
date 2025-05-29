import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.db.connection import get_connection

def setup_db():
    conn = get_connection()
    cursor = conn.cursor()

    with open("lib/db/schema.sql", "r") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_db()
    print("Database setup complete.")
