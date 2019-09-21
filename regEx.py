import re

fhand = open('/Users/rhiannongschwend 1/Desktop/Simon/code/python/code3/mbox-short.txt')

for line in fhand:
   # y = re.findall('^X-DSPAM-Confidence: (\S+)',line)
    y = re.findall('^From: .+@(\S+)',line)
    
    if not len(y) < 1:
         print(y)


