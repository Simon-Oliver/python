has_good_credit = True
price_in_millions = 1000000

if has_good_credit:
    print('You need to pay ' + str(int(price_in_millions * 0.1)))
else:
    print('You need to pay ' + str(int(price_in_millions * 0.2)))
