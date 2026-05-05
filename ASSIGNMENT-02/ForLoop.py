from collections import Counter
VOWELS = "aeiouAEIOU"

def is_prime(number):
    if number < 2:
        return False

    for i in range(2,number):
        if number % i == 0:
            return False

    return True


for i in range(1,11):
    print(i, end=' ')
print("\n=============")
for i in range(10,0,-1):
    print(i, end=' ')
print("\n=============")
for i in range(1,21):
    if i % 2 == 0:
        print(i, end=' ')
print("\n=============")
summation = 0
for i in range (1,101):
    summation += i
print(summation)
print("=============")
length = 0
for character in "Python":
    length += 1
    print(character)
print(length, "characters in the text")
print("=============")
digits = 0
for character in "Nier replicant ver.1_0123123":
    if character.isdigit():
        digits += 1
print(f"There are {digits} digits in the text given above.")
print("=============")
sum_digits = 0
for i in "123abc45":
    if i.isdigit():
        sum_digits += int(i)
print(f"Sum of all digits in the text is {sum_digits}")
print("=============")
for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i% 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
print("=============")
for i in range(1,101):
    if i % 7 == 0:
        print("Skip",end=' ')
        continue
    else:
        print(i, end=' ')
print("\n=============")
list1 = [3,7,2,9,4,5]
print(f"The maximum element in the list is: {max(list1)}")
print("=============")
list2 = [5,12,7,18,3,21]
count = 0
for i in list2:
    if i > 10:
        print(i)
        count += 1
print(f"{count} elements in the list are bigger than 10")
print("=============")
for i in range(1,6):
    for j in range(1,6):
        print(i*j,end='   ')
    print()
print("=============")
for i in range(1,6):
    for j in range(1,6):
        print('*', end='  ')
    print()
print("=============")
for i in range(1,20):
    if is_prime(i):
        print(i, end=' ')
print("\n=============")
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=' ')
print("\n=============")
count2 = 0
for character in "TamerCanTotosStudentInPJATKS32756":
    if character in VOWELS:
        count2 += 1
        print(character, end=' ')
print(f"\nThere are {count2} vowels in the text given above")
print("=============")
for character in "Introduction to Python programming language":
    if character.isspace():
        continue
    print(character, end='')
print()
text = "Introduction to Java programming language101"
print(''.join(c.upper() if c.isalpha() else c for c in text if not c.isspace()))
print("=============")
text_reverse = ""
for i in text:
    if i.isspace():
        continue
    text_reverse = i + text_reverse
print(text_reverse)
print("=============")
text_to_be_counted = "TamerCanTotosS32756StudentAtPjatkInWarsaw"
letter_dictionary = {}
for letter in text_to_be_counted.lower():
    if letter.isalpha():
        if letter in letter_dictionary:
            letter_dictionary[letter] += 1
        else:
            letter_dictionary[letter] = 1
print(letter_dictionary)
print("=============")
list3 = [8,3,15,2,9,11]
print(f"Minimum element in the list is: {min(list3)}")
print("=============")
list4 = [1,2,3,4,5]
multiplication = 1
for i in list4:
    multiplication *= i
print(f"Multiplication of all elements in the list is: {multiplication}")
print("=============")
for i in range(1,101):
    if is_prime(i):
        print(i, end=' ')
print("\n=============")
for i in range(5):
    for j in range(i+1):
        print('*',end='')
    print()
print("=============")
for i in range(5):
    for j in range(5-i):
        print('*',end='')
    print()
print("=============")
list5 = [1,2,3,4]
for i in range(len(list5)):
    for j in range(i+1, len(list5)):
        print(f" {list5[i], list5[j]}", end=' ')
    print()
print("=============")
list6 = [10,5,8,20,3,15]
print(sorted(list6)[-2])
print("=============")
text = "tamercan totosisstudentatcomputerscience"
for letter in text:
    print(' ' if letter.isspace() else chr(ord(letter) - 32), end='')
print("\n=============")
text = "tamercantotoss32756pjatk"
for char in text:
    print(char if char.isalpha() else '', end='')
print("\n=============")
list7 = [4,8,15,16,23,42]
print(f"average of the given list is: {sum(list7) / len(list7)} ")
