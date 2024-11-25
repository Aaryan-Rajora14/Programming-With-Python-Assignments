# 13. Check if a List is Palindromic: Given a list, check if it is a palindrome (reads the same forwards and backwards) using while loop without use of slicing.

lst = [1, 2, 3, 2, 1]

left = 0
right = len(lst) - 1
is_palindrome = True

while left < right:
    if lst[left] != lst[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
    
if is_palindrome:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")