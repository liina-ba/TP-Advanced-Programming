nbr = int(input("Number: "))
if nbr % 3 == 0 and nbr % 5 == 0 :
    print("FizzBuzz")
elif nbr % 5 == 0 :
    print("Buzz")
elif nbr % 3 == 0 :
    print("Fizz")