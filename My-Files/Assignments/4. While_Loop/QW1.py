# 1. Write a python program to accept the string and count the number of upper case character.

while True:
    a = input("Enter a string: ")

    upper = 0

    for char in a:
        if char.isupper():
            upper += 1

    print("Number of uppercase characters:", upper)