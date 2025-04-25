# 6. Write a program that asks the user for two numbers and divides them. Use exception handling to manage the cases where the user enters something that isn't a number or tries to divide by zero.

while True:
    try:
        a = int(input('Enter a Number: '))
        b = int(input('Enter another to divide first Number: '))
        print(f"{a} divided by {b} is {a/b}")            
    except Exception as e:
        print(f"Dont Divide by Zero or Invalid Literals Error!:-\n{e}")