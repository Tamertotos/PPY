import math
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"The number {number} is even")

if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is zero")

binaryVersion = bin(number)
print(binaryVersion)
print(type(binaryVersion))
print(id(number))
print(id(binaryVersion))

hexaVersion = hex(number)
print(hexaVersion)
print(type(hexaVersion))
print(id(hexaVersion))

square = math.pow(number,2)
print(square)
print(type(square))
print(id(square))
