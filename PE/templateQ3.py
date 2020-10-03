import sqlite3
db = sqlite3.connect('test.db')
try:
    cur = db.cursor()
    cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')
    print ('table created successfully')
except:
    print ('error in operation')
    db.rollback()
db.close()
# Example: Create a New Table in Sqlite Copy

import sqlite3
db=sqlite3.connect('test.db')
try:
    cur =db.cursor()
    cur.execute('''CREATE TABLE student (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT (20) NOT NULL,
    age INTEGER,
    marks REAL);''')
    print ('table created successfully')
except:
    print ('error in operation')
    db.rollback()
db.close()

# Example: Insert a Record in Sqlite

import sqlite3
db=sqlite3.connect('test.db')
qry="insert into student (name, age, marks) values('Rajeev', 20, 50);"
try:
    cur=db.cursor()
    cur.execute(qry)
    db.commit()
    print ("one record added successfully")
except:
    print ("error in operation")
    db.rollback()
db.close()

# Example: Inserts a record using the parameter substitution method:

import sqlite3
db=sqlite3.connect('test.db')
qry="insert into student (name, age, marks) values(?,?,?);"
try:
    cur=db.cursor()
    cur.execute(qry, ('Vijaya', 16,75))
    db.commit()
    print ("one record added successfully")
except:
    print("error in operation")
    db.rollback()
db.close()

# The list object (containing tuples) is the parameter of the executemany() method

import sqlite3
db=sqlite3.connect('test.db')
qry="insert into student (name, age, marks) values(?,?,?);"
students=[('Amar', 18, 70), ('Deepak', 25, 87)]
try:
    cur=db.cursor()
    cur.executemany(qry, students)
    db.commit()
    print ("records added successfully")
except:
    print ("error in operation")
    db.rollback()
db.close()

# fetchone(): Fetches the next available record from the result set.
# It is a tuple consisting of values of each column of the fetched record.
# fetchall(): Fetches all remaining records in the form of a list of tuples.
# Each tuple corresponds to one record and contains values of each column in the table.

# Example: Fetch Records
import sqlite3
db=sqlite3.connect('test.db')
sql="SELECT * from student;"
cur=db.cursor()
cur.execute(sql)
while True:
    record=cur.fetchone()
    if record==None:
        break
    print (record)
db.close()

# Example: fetchall()
import sqlite3
myUsers = (
    (1,"trang"),
    (2,"trang2")
)
db=sqlite3.connect('demoSql2.db')
with db:
    cur = db.cursor()
    cur.execute("select * from users")
    rows = cur.fetchall()
    for i in rows:
        print(i)
db.close()

# Update Record
import sqlite3
db=sqlite3.connect('test.db')
qry="update student set age=? where name=?;"
try:
    cur=db.cursor()
    cur.execute(qry, (19,'Deepak'))
    db.commit()
    print("record updated successfully")
except:
    print("error in operation")
    db.rollback()
db.close()

# Delete a Record
import sqlite3
db=sqlite3.connect('test.db')
qry="DELETE from student where name=?;"
try:
    cur=db.cursor()
    cur.execute(qry, ('Bill',))
    db.commit()
    print("record deleted successfully")
except:
    print("error in operation")
    db.rollback()
db.close()
