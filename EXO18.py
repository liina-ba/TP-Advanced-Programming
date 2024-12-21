numbers = [1, 2, 3, 4, 5]

def displayMenu():
    print("\nMenu:")
    print("1. Append an element")
    print("2. Insert an element at a specific position")
    print("3. Pop an element")
    print("4. Remove an element")
    print("5. Sort the list")
    print("6. Reverse the list")
    print("7. Search for an element")
    print("8. Quit")

def appendElement():
    try:
        value = int(input("Enter value to append: "))
        numbers.append(value)
        print("Updated List:", numbers)
    except ValueError:
        print("Invalid input. Please enter an integer.")

def insertElement():
    try:
        value = int(input("Enter value to insert: "))
        index = int(input("Enter index: "))
        if 0 <= index <= len(numbers):
            numbers.insert(index, value)
            print("Updated List:", numbers)
        else:
            print("Index out of range.")
    except ValueError:
        print("Invalid input. Please enter integers for value and index.")

def popElement():
    try:
        index = int(input("Enter index to pop: "))
        if 0 <= index < len(numbers):
            removed = numbers.pop(index)
            print(f"Popped element: {removed}")
            print("Updated List:", numbers)
        else:
            print("Index out of range.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")
    except IndexError:
        print("Cannot pop from an empty list.")

def removeElement():
    try:
        value = int(input("Enter value to remove: "))
        numbers.remove(value)
        print("Updated List:", numbers)
    except ValueError:
        print("Value not found in the list or invalid input.")

def sortList():
    numbers.sort()
    print("List sorted:", numbers)

def reverseList():
    numbers.reverse()
    print("List reversed:", numbers)

def searchElement():
    try:
        value = int(input("Enter value to search: "))
        if value in numbers:
            index = numbers.index(value)
            print(f"Value {value} found at index {index}.")
        else:
            print("Value not found in the list.")
    except ValueError:
        print("Invalid input. Please enter an integer.")


# Main Program
print("Initial List:", numbers)

while True:
    displayMenu()
    try:
        option = int(input("Choose an option: "))
        if option == 1:
            appendElement()
        elif option == 2:
            insertElement()
        elif option == 3:
            popElement()
        elif option == 4:
            removeElement()
        elif option == 5:
            sortList()
        elif option == 6:
            reverseList()
        elif option == 7:
            searchElement()
        elif option == 8:
            break
        else:
            print("Invalid option. Please choose a number between 1 and 8.")
    except ValueError:
        print("Invalid input. Please enter a number.")
