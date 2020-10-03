import sqlite3
db = sqlite3.connect('dbFU.sqlite')
fname = open("datafile.txt")
with db:
    try:
        cur = db.cursor()
        #Create Table
        cur.executescript('''
DROP TABLE IF EXISTS ProStatus;


CREATE TABLE ProStatus (
    ProCode     INTEGER,
    deleted   TEXT
);
''')
        #Insert file txt to database
        for line in fname:
               line = line.rstrip().split()
               cur.execute("Insert into ProStatus (ProCode,deleted) values(?,?)",(int(line[0]),line[3]))
        #get top 5 sorted in des order by ProCode
        cur.execute("select * from ProStatus ORDER by ProCode desc LIMIT 5")
        rows = cur.fetchall()
        for i in rows:
            print(i)

    except:
        print ("error in operation")
        db.rollback()   
db.close()