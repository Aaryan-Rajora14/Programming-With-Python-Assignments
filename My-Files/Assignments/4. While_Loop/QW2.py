# 2.  Write a program to count the number of times a character appears in a given string.

while True:
    a = input("Enter Your String: ")
    word = input("Enter the character you want to count: ")


    count = 0
    for char in a:
        if char == word:
            count += 1

    print(f"The character '{word}' appears {count} times in the string.")
