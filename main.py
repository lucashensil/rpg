import sqlite3

conn = sqlite3.connect('rpg.db')

cursor = conn.cursor()




conn.commit()
conn.close()