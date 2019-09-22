import re

fhand = open('/Users/rhiannongschwend 1/Desktop/Simon/code/python/code3/mbox.txt')
x_list = []


for line in fhand:
    x_spam_con = re.findall('X-DSPAM-Confidence: (\S*)', line)
    if len(x_spam_con) > 0:
        x_list.append(float(x_spam_con[0]))

x_max = max(x_list)
print(len(x_list))