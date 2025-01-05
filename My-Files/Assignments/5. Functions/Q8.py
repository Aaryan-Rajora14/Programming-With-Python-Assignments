# 8.  Write a Python function that accepts a string and counts the number of upper and lower case letters.

def count_letters(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

while True:
    string = input('Type Your Words: ')
    upper, lower = count_letters(string)
    print(f"Uppercase letters: {upper}")
    print(f"Lowercase letters: {lower}")
