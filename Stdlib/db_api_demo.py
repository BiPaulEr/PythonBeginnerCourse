import sqlite3
import os

absolute_path = os.path.join(os.path.dirname(__file__), "database.db")
conn = sqlite3.connect(absolute_path)

cur = conn.cursor()
"""
cur.execute(""
    CREATE TABLE employees (
            id INTEGER PRIMARY KEY,
            name VARCHAR(20),
            balance DECIMAL(6,2)
            )"")"""
"""
cur.execute("INSERT INTO employees (name, balance)  VALUES ('DUPONT', 200)")
"""
"""
cur.executemany(" INSERT INTO employees (name, balance) VALUES (?, ?)",
            [("Jean", 500), ("RIOLO", 700)])
conn.commit()
"""
def getBalance(cursor, balance, operator ="<"):
    cursor.execute(f"SELECT * FROM employees WHERE balance {operator} ?", (balance,))
    for row in cursor.fetchall():
        print(row)
getBalance(cur, 1000, "!=")
"""     
cur.execute("SELECT * FROM employees")

for row in cur.fetchall():
    print(row)
"""
cur.close()
conn.close()
