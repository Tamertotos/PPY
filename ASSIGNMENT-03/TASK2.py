import keyword
user_names = set()

while len(user_names) < 5:
    name = input("Enter a user to be added")

    if name in user_names:
        print("This person already exists in the set")
        continue

    if name.isalpha() and not keyword.iskeyword(name):
        user_names.add(name)
    else:
        print("OI")
        continue

my_list = list(user_names)
my_list.sort()
print(f"After sorting the set {my_list} ")
print(f"Number of unique users is: {len(user_names)}")

t = tuple(my_list[i] for i in range(3) )
print(t)

print(f"The longest name in the list: {max(my_list, key=len)}")

user1 = input("Enter first user to check: ")
user2 = input("Enter second user to check: ")

if user1 in my_list and user2 in my_list:
    print(f"{user1} and {user2} in the list")
else:
    print("Either or neither of them exists in the list!!!")

portion = my_list[1:3]
print(portion)
print(f"The longest name in the portion: {max(portion, key=len)}")