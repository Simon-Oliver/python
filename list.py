numbers = [10, 1109, 55, 200, 33, 60, 102]
largest = numbers[0]

for number in numbers:
    if largest < number:
        largest = number
print(largest)
