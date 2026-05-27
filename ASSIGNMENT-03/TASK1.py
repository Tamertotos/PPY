WIDTH = 40
shopping_list = dict()

while len(shopping_list) < 4:

    name = input("Please enter an item name\n")

    try:
        price = int(input("Please enter its price\n"))
    except ValueError:
        print("Enter a numerical value!")
        continue

    shopping_list[name] = price


average = sum(shopping_list.values())/len(shopping_list)
print("*"*WIDTH)
print(f"{'RECEIPT':^{WIDTH}}")
print("*"*WIDTH)
print(f"{'Total value:':<{WIDTH-10}}{sum(shopping_list.values()):>10}")
print(f"{'Most expensive:':<{WIDTH-10}}{max(shopping_list, key=shopping_list.get):>10}")
print(f"{'The average price:':<{WIDTH-10}}{average:>{10}.2f}")