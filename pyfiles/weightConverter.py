weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ').lower()

if unit == 'k':
    lbs = weight / 0.45
    print(f'You are {lbs} Lbs')
elif unit == 'l':
    kg = weight * 0.45
    print(f'You are {kg} Kilos')
else:
    print('Not a valid unit')
