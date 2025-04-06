import sqlite3

def init_db():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_summary (
            id INTEGER PRIMARY KEY,
            city TEXT,
            date TEXT,
            avg_temp REAL,
            max_temp REAL,
            min_temp REAL,
            dominant_condition TEXT
        )
    ''')
    conn.commit()
    conn.close()

def store_daily_summary(summary):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO weather_summary (city, date, avg_temp, max_temp, min_temp, dominant_condition)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        summary['city'],
        summary['date'],
        summary['avg_temp'],
        summary['max_temp'],
        summary['min_temp'],
        summary['dominant_condition']
    ))
    conn.commit()
    conn.close()
