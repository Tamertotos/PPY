import random

number = random.randint(0,100)

lst = []

while True:
    guessed_number = int(input("Pick a number\n"))
    lst.append(guessed_number)


    if guessed_number > number:
        print("Too big, try a smaller value")
    elif guessed_number < number:
        print("Too small, try a bigger value")
    else:
        print("Congrats! You found it")
        break


print(lst)
print(f"guessed a number {len(lst)} times")
print(f"Last 3 guesses are: {lst[-3:]}")