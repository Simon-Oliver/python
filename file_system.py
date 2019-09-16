fileName = input('Enter File Name: ')
# mbox.txt

try:
    fhand = open('./code3/' + fileName, 'r')
except:
    print('File cannot be opened: ', fileName)
    quit()

count = 0
email = []

for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        email.append(line.strip('From: '))
    count += 1



# inp = fhand.read()
#
print(len(email))