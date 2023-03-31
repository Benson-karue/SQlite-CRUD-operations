import sqlite3

conn = sqlite3.connect("employee.db")
print('successfully connected')

data = conn.execute("SELECT * FROM Staff")
for rows in data:
    print("ID: ",rows[0])
    print("FIRSTNAME: ",rows[1])
    print("LASTNAME: ",rows[2])
    print("AGE: ",rows[3])
    print("TASK: ",rows[4])
    
print('successfully fetched data')
conn.close()
