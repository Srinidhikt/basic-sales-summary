import sqlite3

conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(sales)")
columns = cursor.fetchall()

print("Columns in 'sales' table:")
for col in columns:
    print(col[1])

conn.close()
