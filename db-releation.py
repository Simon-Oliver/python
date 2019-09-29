import xml.etree.ElementTree as ET
import sqlite3

# connect = sqlite3.connect('tracks.db')
# db = connect.cursor()

# db.executescript('''
# DROP TABLE IF EXISTS Artist;
# DROP TABLE IF EXISTS Album;
# DROP TABLE IF EXISTS Track;

# CREATE TABLE Artist (
#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name TEXT UNIQUE
# );


# CREATE TABLE Album (
#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     title TEXT UNIQUE,
#     artist_id INTEGER
# );

# CREATE TABLE Track (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     title TEXT UNIQUE,
#     album_id INTEGER,
#     len INTEGER
#     rating INTEGER,
#     count INTEGER

# );
# ''')

fhandle = open('./code3/tracks/Library.xml')


def lookup(data, key):
    found = False
    for child in data:
        if found:
            print(child.TEXT)
