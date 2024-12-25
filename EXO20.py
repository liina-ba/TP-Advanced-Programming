import statistics

user_list = []
# 4- Load and append to an existing list.
try:
    with open("user_list.txt", "r") as file:
        content = file.read()
        if content:
            user_list = list(map(int, content.split(", ")))
            print("Loaded List: ", user_list)
        else:
            print("The file is empty. Starting with an empty list.")
except FileNotFoundError:
    print("No existing list found.")

while True:
    user_input = input("Enter a number (0 to quit) : ")
    try:
        number = int(user_input)
        if number == 0:
            break
        user_list.append(number)
        print("Current List : ", user_list)
        print("Sorted List: ", sorted(user_list))

        # Bonus Features
        # 1-Descending Order
        print("Descending List:", sorted(user_list, reverse=True))
        # 2-List Statistics
        mean = statistics.mean(user_list)
        print("Mean:", mean)
        median = statistics.median(user_list)
        print("Median:", mean)
        # 3-Allow users to save the list to a file.
        with open("user_list.txt", "w") as file:
            file.write(", ".join(map(str,
                                     user_list)))  # since join works only with string we convert user_list elements to strings using map and str and we use join methode to concatinate all the elements into a single string separated with ","
        print("List saved to user_list.txt")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
