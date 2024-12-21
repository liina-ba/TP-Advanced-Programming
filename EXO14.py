word = input("Word: ")

maxWidth = 30
contentWidth = maxWidth - 2  # for the * in the borders
leftSpace = (contentWidth - len(word)) // 2
rightSpace = contentWidth - len(word) - leftSpace  # Remaining space in the content

print("*" * maxWidth)
print("*" + " " * leftSpace + word + " " * rightSpace + "*")
print("*" * maxWidth)  
