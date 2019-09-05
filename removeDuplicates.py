numbers = [2, 6, 3, 8, 9, 3, 7]
no_duplicates = []

for number in numbers:
    if number not in no_duplicates:
        no_duplicates.append(number)

print(no_duplicates)
