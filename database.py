import sqlite3

def connect():
    return sqlite3.connect("study.db")

def setup():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS subjects(
        id INTEGER PRIMARY KEY,
        name TEXT,
        exam_date TEXT,
        priority INTEGER,
        hours INTEGER
    )""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS sessions(
        id INTEGER PRIMARY KEY,
        subject TEXT,
        hours REAL,
        date TEXT
    )""")

    conn.commit()
    conn.close()
