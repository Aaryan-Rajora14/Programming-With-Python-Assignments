# 3. Write a Program in python to display a menu for calculating area of a circle & perimeter of a circle. 

while True:
    r = int(input("Enter Racdius of Circle"))
    pie = 22/7
    ch = input("Enter Choice for 'A' for Area 'C' for Cicumference :")
    if ch == 'A':
        a= pie*r*r
        print(f"\nArea of Circle is {a}")
    elif ch == "C":
        c=2*pie*r
        print(f"\nCircumference of Circle is {c}")