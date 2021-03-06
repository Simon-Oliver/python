import sqlite3

connect = sqlite3.connect('sqlexploration.db')
db = connect.cursor()

db.execute('CREATE TABLE IF NOT EXISTS Task (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, user_id INTEGER)')
db.execute('CREATE TABLE IF NOT EXISTS User (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE, task_id INTEGER)')

user = ''
task = ''
new_task = True

while True:
    while len(user) < 1:
        user = input('Please enter username: ')

    while len(task) < 1:
        task = input('Enter Task: ')

    db.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (user,))
    db.execute('SELECT id FROM User WHERE name=?', (user,))
    user_id = db.fetchone()[0]
    db.execute('INSERT OR IGNORE INTO Task (title, user_id) VALUES (?,?)',
               (task, user_id))
    connect.commit()

    user = ''
    task = ''
    print(user_id)
