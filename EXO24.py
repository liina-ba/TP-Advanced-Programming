def anagrams(str1, str2):
    str1 = str1.lower()  #make it not sensitive to case
    str2 = str2.lower()

    return sorted(str1) == sorted(str2)  # sorting the strings to make them the same if they are anagrams

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

print(anagrams(str1, str2))