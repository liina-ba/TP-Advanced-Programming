numbers = []
shoe_sizes = []

for nbr in [1, 2, 3, 4, 5]:
    numbers.append(nbr)

for size in [8, 9, 10, 11, 12]:
    shoe_sizes.append(size)

print("Numbers List:", numbers)
print("Shoe Sizes List:", shoe_sizes)

#Bonus:
# 1- Handling duplicates numbers
numbers.append(3)
numbers = list(set(numbers)) # a set is known by not having duplicates so converting numbers to a set will remove duplicates and then go back to a list

# 2-Combining numbers and shoe_sizes into a third list
combined_list = numbers + shoe_sizes
print("Combined List :", combined_list)