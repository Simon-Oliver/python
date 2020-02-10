import json
import re
import sqlite3

connect = sqlite3.connect('flavour.db')
db = connect.cursor()

db.execute('DROP TABLE IF EXISTS Pairing')
db.execute('CREATE TABLE Pairing (name TEXT, category TEXT, pairing TEXT)')

with open('combinations.json') as json_file:
    data = json.load(json_file)
    for n in data:
        obj ={}
        ing = []

        name = re.findall('flavordb.\w*.(.*)',n['name'])
        category = re.findall('flavordb.(\w*).\w*',n['name'])

        for i in n['imports']:
            ingredient = re.findall('flavordb.\w*.(\w*)',i)
            if len(ingredient) < 1: continue
            ing.append(ingredient[0])
        obj['name'] = name[0]
        obj['category'] = category[0]
        obj['match'] = ing
        db.execute('INSERT INTO Pairing (name, category, pairing) VALUES (?, ?, ?)', (name[0], category[0], str(ing)))
        connect.commit()
        print(obj)




