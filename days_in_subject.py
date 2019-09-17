data = open('code3/mbox.txt')

for line in data:
    if 'From ' in line:
        words = line.split()
        print(words[2])