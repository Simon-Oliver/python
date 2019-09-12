name = input('Please enter your name: ')
name_len = len(name)

if name_len < 3:
    print('Must be longer than 3 characters')
elif name_len > 50:
    print('Name must be less than 50 characters')
else:
    print(name)
