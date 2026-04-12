import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("factory.db")
    cursor= conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor_readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT NOT NULL,
            value TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def save_reading(topic, value):
    conn = sqlite3.connect("factory.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO sensor_readings (topic, value, timestamp)
        VALUES (?, ?, ?)
    """, (topic, value, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def get_latest_readings():
    conn = sqlite3.connect("factory.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT topic,value, timestamp
        FROM sensor_readings
        ORDER BY id DESC
        LIMIT 10
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows


if __name__ == "__main__":
    init_db()
    print("Database created succesfully")