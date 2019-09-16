fhand = open('test.txt', 'r')


count = 0

for data in fhand:
    data = data.rstrip()
    count += 1
    print(data)


# inp = fhand.read()
#
# print(inp)