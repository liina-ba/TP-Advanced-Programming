def calculateDiscount():
    totalAmount = float(input("Total amount: "))
    nbrItems = int(input("Number of items: "))
    dayOfWeek = input("Day of the week: ")

    discount = 0
    if dayOfWeek in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        discount += 10
    elif dayOfWeek in ["Saturday", "Sunday"]:
        discount += 20
    else:
        print("Invalid day of the week. Please enter a valid day.")
        return

    if nbrItems >5 :
        discount+=5

    totalPrice = totalAmount *(1 - discount/100)

    print(f"Total price after discount: {totalPrice:.2f} dinars")



calculateDiscount()