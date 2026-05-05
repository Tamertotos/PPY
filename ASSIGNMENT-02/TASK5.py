user_names = []

def search_user(name,user_name):
    if name in user_name:
        index = user_name.index(name)
        print(f"The user {name} exists under the {index} index.")
    else:
        print(f"Given user {name} does not exists in the list")

while len(user_names) < 8:
    name = input("Enter a user name to save in a list.\n").lower()

    if  not name.isalpha():
        print("Only names are allowed, no numbers!")
        continue

    if name in user_names:
        print(f"This person {name} already exists")
        continue

    user_names.append(name)

if user_names:
    user_names.sort()
    print(f"Alphabetically sorted list: {user_names}")
    print(f"First 5 users {user_names[:5]}")
    print(f"The longest username: {max(user_names, key=len)}")
    print(f"The shortest username: {min(user_names, key=len)}")

search = input("Search for a username:\n").lower()
search_user(search,user_names)