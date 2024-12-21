numbers = [1,2,3,4,5]

while True:
    try:
        index = int(input("Enter index (-1 to exit): "))
        if index == -1:
            break
        if index < 0 or index>= len(numbers):
            print("Invalid index. Please enter a valid index.")
            continue
        newValue = input("Enter new Value: ")
        try:
            newValue = int(newValue)
        except ValueError:
            print("Invalid value. Please enter an integer.")
            continue
        numbers[index] = newValue
        print(numbers)
    except ValueError:
        print("Invalid input. Please enter a valid integer index.")
