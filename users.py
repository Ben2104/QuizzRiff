import sqlite3

conn = sqlite3.connect("user_data.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO users (username, password, score) VALUES ('DIANOOSH', 'ADMIN', 1021)")
cursor.execute("INSERT INTO users (username, password, score) VALUES ('ALEX', 'ADMIN', 1020)")
cursor.execute("INSERT INTO users (username, password, score) VALUES ('KAYDEE', 'ADMIN', 1019)")

conn.commit()
