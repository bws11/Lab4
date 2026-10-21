print("Welcome to the vending machine!")
working = True
balance = 200

items = {
    "Crisps": 100,
    "Chocolate": 150,
    "Water": 120
}

while working:
    print(f"Your balance is {balance}p")
    user_input = int(input("1. Crisps - 100p\n2. Chocolate - 150p\n3. Water - 120p\n4. Exit\nEnter an option: "))
    
    if user_input == 1:
        if balance >= items["Crisps"]:
            balance -= items["Crisps"]
        else:
            print("Can't purchase")

    elif user_input == 2:
        if balance >= items["Chocolate"]:
            balance -= items["Chocolate"]
        else:
            print("Can't purchase")

    elif user_input == 3:
        if balance >= items["Chocolate"]:
            balance -= items["Water"]
        else:
            print("Can't purchase")

    elif user_input == 4:
        working = False

    else:
        print("Invalid input")

