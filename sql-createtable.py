import sqlite3

conn = sqlite3.connect('employee.db')
print('connected successfully')

conn.execute("""CREATE TABLE staff1(
 ID INT PRIMARY KEY NOT NULL,
 FIRSTNAME TEXT NOT NULL,
 LASTNAME TEXT NOT NULL,
 AGE INT,
 TASK TEXT CHAR(20))
 
""")

print('successfully created staff ')
conn.close()
