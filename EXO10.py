word = input("enter a word: ")

isPalindrome = True

for i in range(len(word)// 2):
    if word[i] != word[len(word)-i-1]:
        isPalindrome = False
        break

if isPalindrome:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")