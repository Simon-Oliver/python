import json
fhand = open('/Users/Simon/Desktop/Coding/python/licenced_electricians.json')

data = json.load(fhand)
min_data = data[:10]

for item in min_data:
    print(item)