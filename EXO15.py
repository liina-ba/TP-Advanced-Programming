#Create a program that asks the user to input a string and checks
# whether certain vowels (a, e, o) are present in the string.

userInput = input("Please type in a string: ")
vowels = ['a','e','o']

for V in vowels:
    if V in userInput:
        print(f"{V} found")
    else:
        print(f"{V} not found")

