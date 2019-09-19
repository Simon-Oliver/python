d = {'a': 10, 'b': 1, 'c': 99}
temp = []

for key,value in sorted(d.items()):
    print(value, key)
    temp.append((value,key))

print(sorted(temp,reverse=True))