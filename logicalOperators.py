has_good_credit = True
has_high_income = False
has_criminal_record = True

if has_high_income or has_good_credit and not has_criminal_record:
    print('Eligable')
elif has_criminal_record:
    print('Not eligable because of criminal record!')
else:
    print('Not eligable!')
