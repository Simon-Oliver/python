import sqlite3
fhand = open('code3/romeo-full.txt')

conn = sqlite3.connect('worddb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (word TEXT, count INTEGER)')

for line in fhand:
    pieces = line.split()
    for piece in pieces:
        cur.execute('SELECT count FROM Counts WHERE word = ? ', (piece,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts (word, count) VALUES (?, 1)', (piece,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE word = ?', (piece,))
        conn.commit()


sqlstr = 'SELECT word, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])