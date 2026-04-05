number = int(input("Enter a number: "))

if number > 0 and number % 2 == 0:
    print(number, "is even and positive")

if  not (number > 0) or number > 100:
    print(number, "is negative OR greater than 100")

