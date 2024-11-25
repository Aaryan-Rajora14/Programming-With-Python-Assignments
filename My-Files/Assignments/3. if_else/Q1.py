#  1. Write a program that takes three numbers as input and prints the largest among them.

x = int(input("Enter First numbers:::"))
y = int(input("Enter Second numbers:::"))
z = int(input("Enter Third numbers:::"))

if x > y and x > z:
    _max = x
   
elif y > x and y > z:
    _max = y
   
else:
    _max = z

print(f"\nMaximum number is {_max}")