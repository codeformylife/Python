import sqlite3 as lit
fname = open("PE/dataQ2.txt")
db = lit.connect("PE/PEQ2.sqlite")
lst = list()
with db:
   cur = db.cursor()
#Tao bang kt trong database
   cur.executescript('''
  
   DROP TABLE IF EXISTS kt;

   CREATE TABLE kt (
   name TEXT (20),
   quality INTEGER NOT NULL,
   price INTEGER);
    ''')
#Insert file txt to database
   for line in fname:
       line = line.rstrip().split()
       lst.append(line)
   cur.executemany("Insert into kt values(?,?,?)",lst[1:])
#Select top 5 sp co so tien ban duoc nhieu
   cur.execute("select * from kt ORDER by price*quality desc LIMIT 5")
   rows = cur.fetchall()
   for i in rows:
       print(i)

