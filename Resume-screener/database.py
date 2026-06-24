import sqlite3

conn = sqlite3.connect("resume.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS candidates(
id INTEGER PRIMARY KEY AUTOINCREMENT,
resume_name TEXT,
score REAL
)
""")

conn.commit()