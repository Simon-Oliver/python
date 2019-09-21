import re

fhand = open('/Users/rhiannongschwend 1/Desktop/Simon/code/python/code3/mbox-short.txt')
obj = {}
temp = []


for line in fhand:
   # y = re.findall('^X-DSPAM-Confidence: (\S+)',line)
    y = re.findall('^From: .+@(\S+)',line)
    
    if not len(y) < 1:
        obj[y[0]] = obj.get(y[0], 0) + 1


for key,value in obj.items():
    temp.append((value,key))

temp = sorted(temp, reverse=True)

for value,key in temp:
    print(key,value)
    