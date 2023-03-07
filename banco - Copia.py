import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("SELECT * FROM users")
jogos = cur.fetchall()
print(jogos)
conn.close()
