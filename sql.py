import sqlite3

connection=sqlite3.connect("student.db")
cursor=connection.cursor()

tabel_info="""
 create table Student(NAME varchar(20),class Varchar(20),section varchar(20),marks INT);
"""

cursor.execute(tabel_info)

##insert Data

cursor.execute('''   INsert into STUDENT Values('Sai', 'Data Science','A', 20)''')
cursor.execute('''   INsert into STUDENT Values('Asif', 'Physic','A', 40)''')
cursor.execute('''   INsert into STUDENT Values('Mit', 'Data Science','B', 90)''')
cursor.execute('''   INsert into STUDENT Values('Mehreen', 'Physic','B', 30)''')
cursor.execute('''   INsert into STUDENT Values('Gaurav', 'Data Science','A', 10)''')


print("Data :\n")
data=cursor.execute("Select * from Student")

for x in data:
    print(x)

connection.commit()
connection.close()