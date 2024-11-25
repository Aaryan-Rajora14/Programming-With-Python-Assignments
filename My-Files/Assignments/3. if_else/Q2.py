# 2. Write a program that takes three numbers and print them in ascending

a = int(input('Enter First Number: '))
b = int(input('Enter Second Number: '))
c = int(input("Enter Third Number: "))

if a > b and a > c:
    _max = a
    if b > c:
        mid = b
        _min = c
    else:
        mid = c
        _min = b

elif b > a and b > c:
    _max = b
    if a > c:
        mid = a
        _min = c
    else:
        mid = c
        _min = a

else:
    _max = c
    if a > b:
        mid = a
        _min = b
    else:
        mid = b
        _min = a

print(f"All the Numbers in ascending order:: {_min},{mid},{_max}")