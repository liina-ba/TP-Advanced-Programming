def uniqueWord_counter():
    """
    Tracks unique words entered by the user until a duplicate is found.
    """
    unique_words = set()
    total_word_count = 0


    while True:
        word = input("Enter a word: ").strip().lower()  # .strip() to remove leading/trailing whitespace
        #.lower() Bonus: Making the program case-insensitive by converting input to lowercase.
        total_word_count += 1

        if word in unique_words:
            print(f"\nDuplicate word detected!")
            print(f"Total words entered: {total_word_count}")
            print(f"Unique words alphabetically: {', '.join(sorted(unique_words))}") # .join() Combines elements of the list returned by sorted() into a single string.
            break
        else:
            unique_words.add(word)






# Run the program
uniqueWord_counter()
