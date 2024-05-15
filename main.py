cart = {}

def addItem():
    itemName = input("Enter item name: ")
    itemPrice = int(input("Enter item price: "))
    return itemName, itemPrice

def printReceipt(cart):
    if not cart:
        print("No item in the cart.")
    else:
        print("Receipt:")
        for item, price in cart.items():
            print(f"{item}: {price}")
        totalPrice = sum(cart.values())
        print("Total price:", totalPrice)

while True:
    print("Menu:")
    print("1. Add item")
    print("2. Print receipt")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        while True:
            itemName, itemPrice = addItem()
            cart[itemName] = itemPrice
            choice = input("Do you want to add another item? (yes/no): ")
            if choice.lower() != 'yes':
                break
    elif choice == '2':
        printReceipt(cart)
        if not cart:
            continue
        else:
            break
    else:
        print("Invalid choice. Please enter 1 or 2.")