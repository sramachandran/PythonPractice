import sqlite3
conn=sqlite3.connect('test.sqlite3')
cur=conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')

cur.execute('''CREATE TABLE Ages(name TEXT,age INTEGER)''')

cur.execute('''DELETE FROM Ages''')


cur.execute('''INSERT INTO Ages (name,age) VALUES ('Faria','18')''')
cur.execute('''INSERT INTO Ages (name,age) VALUES ('J','15')''')
cur.execute('''INSERT INTO Ages (name,age) VALUES ('Zosia','20')''')
cur.execute('''INSERT INTO Ages (name,age) VALUES ('Keo','40')''')


conn.commit()

resultHex = cur.execute('''SELECT hex(name || age) AS X FROM Ages ORDER BY X''')
print(resultHex)