import sqlite3

conn = sqlite3.connect('employee.db')
print('successfully connected to the database')

conn.execute('DELETE FROM Staff where id=4')
conn.commit()

data = conn.execute('select * from staff')
for rows in data:
    print('id ', rows[0])
    print('firstname ', rows[1])
    print('lastname ', rows[2])
    print('age ', rows[3])
    print('task ', rows[4])

print("successfully deleted a row")
conn.commit()
