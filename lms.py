import csv
import sqlite3

connect = sqlite3.connect('lms.db')
db = connect.cursor()

# id,first_name,last_name,email,gender,university,department,course

db.execute('''
CREATE TABLE IF NOT EXISTS Student (
id INTEGER PRIMARY KEY AUTOINCREMENT,
s_id INTEGER NOT NULL UNIQUE,
first_name TEXT,
last_name TEXT,
email TEXT,
gender_id INTEGER,
university_id INTEGER,
department_id INTEGER,
course_id INTEGER)
''')

db.execute('CREATE TABLE IF NOT EXISTS Gender (id INTEGER PRIMARY KEY AUTOINCREMENT, gender TEXT UNIQUE)')
db.execute('CREATE TABLE IF NOT EXISTS University (id INTEGER PRIMARY KEY AUTOINCREMENT, university TEXT UNIQUE)')
db.execute('CREATE TABLE IF NOT EXISTS Department (id INTEGER PRIMARY KEY AUTOINCREMENT, department TEXT UNIQUE)')
db.execute('CREATE TABLE IF NOT EXISTS Course (id INTEGER PRIMARY KEY AUTOINCREMENT, course TEXT UNIQUE)')

with open('MOCK_DATA.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count is 0:
            line_count += 1

        print(row['course'])
        # Create/Select course_id
        db.execute('INSERT OR IGNORE INTO Course (course) VALUES (?)', (row['course'],))
        db.execute('SELECT id FROM Course WHERE course=?', (row['course'],))
        course_id = db.fetchone()[0]

        # Create/Select department_id
        db.execute('INSERT OR IGNORE INTO Department (department) VALUES (?)', (row['department'],))
        db.execute('SELECT id FROM Department WHERE department=?', (row['department'],))
        department_id = db.fetchone()[0]

        # Create/Select university_id
        db.execute('INSERT OR IGNORE INTO University (university) VALUES (?)', (row['university'],))
        db.execute('SELECT id FROM University WHERE university=?', (row['university'],))
        university_id = db.fetchone()[0]

        #Create/Select gender_id
        db.execute('INSERT OR IGNORE INTO Gender (gender) VALUES (?)', (row['gender'],))
        db.execute('SELECT id FROM Gender WHERE gender=?', (row['gender'],))
        gender_id = db.fetchone()[0]

        #Create Student
        db.execute('INSERT OR IGNORE INTO Student (s_id, first_name, last_name, email, gender_id, university_id, department_id, course_id) VALUES (?, ?, ?, ?, ?, ?,?, ? )',
                   (row['id'], row['first_name'], row['last_name'], row['email'], gender_id, university_id, department_id, course_id))
        line_count += 1
        print(line_count)
        connect.commit()

    print(f'Processed {line_count} lines.')