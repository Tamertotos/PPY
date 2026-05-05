shopping_cart = []

print("Press 0 to exit.")

while True:
    try:
        price = int(input("Input a price tag for a product.\n"))
    except ValueError:
        print("Enter a valid number!")
        continue

    if price == 0:
        break

    shopping_cart.append(price)

if shopping_cart:
    print(f"Total price is: {sum(shopping_cart)}")
    print(f"The most expensive item is: {max(shopping_cart)}")
    print(f"The average is: {sum(shopping_cart)/len(shopping_cart):.2f}")
    print(f"shopping cart in reverse: {shopping_cart[::-1]}")
else:
    print("Your cart is empty")
