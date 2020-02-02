numRange = range(101)

for num in numRange:
    response = ""
    if num % 3 == 0:
        response += "Fizz"
    if num % 5 == 0:
        response += "Buzz"

    print(response or num)
