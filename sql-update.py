import sqlite3

conn = sqlite3.connect('employee.db')
print('connected successfully')

conn.execute("UPDATE staff set age=45 where ID=4")
conn.commit()

data = conn.execute("SELECT * FROM Staff")
for rows in data:
    print("ID: ", rows[0])
    print("FIRSTNAME: ", rows[1])
    print("LASTNAME: ", rows[2])
    print("AGE: ", rows[3])
    print("TASK: ", rows[4])

print("salary successfully changed")
conn.close