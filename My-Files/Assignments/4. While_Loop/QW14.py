# 14. Remove All Occurrences of a Specific Element: Given a list, remove all occurrences of a specific element using a while loop.

numbers = [1,2,7,3,8,7,5,9,7,4,12,7]
element = 7

while element in numbers:
    numbers.remove(element)
    
print(numbers)