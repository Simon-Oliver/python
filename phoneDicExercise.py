digit = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine'
}

phone_num = input('Phone: ')
number_txt = ''
for number in phone_num:
    number_txt += f'{digit.get(int(number))} '

print(number_txt)
