import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org  TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    # Get the domains
    words = line.split()
    org = words[1].split("@")
    cur.execute('SELECT count FROM Counts WHERE org  = ? ', (str(org[1]),))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (str(org[1]),))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (str(org[1]),))
conn.commit()

