birth_year = int(input('Enter birth year: '))

while 2019 - birth_year < 18:
    print(f'Your only {2019 - birth_year} years old.')
    birth_year = int(input('Enter birth year: '))
print('Welcome')
