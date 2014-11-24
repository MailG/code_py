
import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("create table stocks (symbol text, shares integer, price real)")
conn.commit()
