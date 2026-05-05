count = 0
while count < 5:

    user_number = int(input("Enter an integer value. Enter a number greater than 100 to exit."))
    if user_number > 100:
        print("Breaking out of loop.")
        break

    count+=1
else:
    print("No number exceeded 100")






# text = "TamercanTotosPJATKS32756"
# i = 0
# while i < len(text):
#
#     if text[i].isdigit():
#         print("\ndigit found breaking...")
#         break
#
#     print(text[i], end='')
#     i += 1
# else:
#     print("No digits in the text")
#
#
#

# attempts = 0
# password = ''
# while password != "python":
#     password = input("Enter your password\n")
#     attempts += 1
#     if attempts > 3:
#         print("Too many attempts, access denied")
#         break
# else:
#     print("Logged in!")
#



# list1 = [3,7,4,8,2]
#
# i = 0
# while i < len(list1):
#     if list1[i] == 10:
#         print("Found 10")
#         break
#     i += 1
# else:
#     print("Number not found!")
#
#

# number = int(input("Give a number to be checked whether it is a prime or not"))
# i = 2
# while i < number:
#     if number % i == 0:
#         print("Not a prime")
#         break
#     i += 1
# else:
#     print("Given number is a prime number!")
#




# summation = 0
# count = 0
# while count < 5:
#     try:
#         numbers = int(input("Enter numbers. Enter 0 or negative numbers to exit."))
#     except ValueError:
#         print("Enter numbers!")
#
#
#     if numbers == 0:
#         print("0 entered, quitting...")
#         break
#
#     if numbers < 0:
#         print("negative number entered, quitting...")
#         break
#
#     summation += numbers
#     count += 1
# else:
#     print("End of data input.")
#
#
# print(f"sum of all numbers is: {summation}, in total {count}  numbers entered")