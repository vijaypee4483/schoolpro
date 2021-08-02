import sqlite3

rollno=str(1000)
# Create a SQL connection to our SQLite database
con = sqlite3.connect("student.sqlite")

cursor = con.cursor()

# The result of a "cursor.execute" can be iterated over by row
row=cursor.execute('SELECT * FROM sdetail where rollno=(?)',(rollno,))
row=cursor.fetchall()
for list in row:
    print(list[5])

# Be sure to close the connection
con.close()