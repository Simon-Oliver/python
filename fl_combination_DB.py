import json
import re

with open('combinations.json') as json_file:
    data = json.load(json_file)
    for n in data:
        obj ={}
        ing = []

        name = re.findall('flavordb.\w*.(\w*)',n['name'])

        for i in n['imports']:
            ingredient = re.findall('flavordb.\w*.(\w*)',i)
            if len(ingredient) < 1: continue
            ing.append(ingredient[0])
        obj['name'] = ing
        print(obj)
