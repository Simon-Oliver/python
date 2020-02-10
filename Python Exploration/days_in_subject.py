data = open('code3/mbox.txt')
ext = []

for line in data:
    if 'From ' in line:
        words = line.split()
        email = words[1]
        pieces = email.split('@')
        if len(pieces) < 2:
            continue
        print(words)
        print(pieces[1])