def ticketPurcahse():
    name = input("Please enter your name: ")
    if name == "VIP" :
        print("Enjoy the Show for free!")
    else:
        tickets = int(input("How many tickets would you like to buy?"))
        if tickets < 0:
            print("Invalid number of tickets.")
            return
        totalCost = tickets * 15.50
        print(f"The total cost is {totalCost:.2f}")
        print("Enjoy your tickets!")

ticketPurcahse()