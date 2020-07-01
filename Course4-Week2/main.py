import sqlite3
conn = sqlite3.connect('Course4-Week2\\asg2.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = "Course4-Week2\data.txt"
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):continue
    pieces = line.split()[1]
    organization = pieces.split("@")[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (organization,))
    row = cur.fetchone()
    if row is None:
        cur.execute(
            '''INSERT INTO Counts (org, count) VALUES (?, 1)''', (organization,))
    else:
        cur.execute(
            'UPDATE Counts SET count = count + 1 WHERE org = ?', (organization,))

conn.commit()
#check data
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
   print(str(row[0]), row[1])
cur.close()
