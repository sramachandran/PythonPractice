import sqlite3
conn=sqlite3.connect('test.sqlite3')
cur=conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''CREATE TABLE Counts(email TEXT,count INTEGER)''')

fname=input("Enter file name:")
if len(fname)<1:mbox-short.txt
fh=open(fname)
for line in fh:
    if not line.startswith("From:"):continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('Select count from Counts where email=?', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''insert into counts(email,count) values(?,1)''', (email,))
    else:
        cur.execute('''update counts set count=count+1 where email=?''',(email,))
    conn.commit()

table = cur.execute('select * from Counts')
print(table)
