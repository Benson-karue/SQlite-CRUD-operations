import sqlite3

conn = sqlite3.connect('employee.db')
print('connected')

conn.execute("INSERT INTO Staff1(ID,FIRSTNAME,LASTNAME,AGE,TASK)\
              VALUES(1,'JOHN','MIKE',25,'sales manager')")
conn.execute("INSERT INTO Staff(ID,FIRSTNAME,LASTNAME,AGE,TASK)\
          VALUES(2,'Angela','angie',30,'sales manager')")
conn.execute("INSERT INTO Staff(ID,FIRSTNAME,LASTNAME,AGE,TASK)\
              VALUES(3,'steve','maina',40,'sales manager')")
conn.execute("INSERT INTO Staff(ID,FIRSTNAME,LASTNAME,AGE,TASK)\
              VALUES(4,'lucy','msoo',23,'sales manager')")

conn.commit()
print("inserted values successfully")
conn.close()