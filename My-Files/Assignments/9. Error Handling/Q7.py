# 7. Modify the program from question 6 to include an else block that prints "Operation successful" if no exceptions are raised.


while True:
    try:
        a = int(input('Enter a Number: '))
        b = int(input('Enter another to divide first Number: '))
        print(f"{a} divided by {b} is {a/b}")            
    except Exception as e:
        print(f"Dont Divide by Zero or Invalid Literals Error!:-\n{e}")
        
    else:
        print("Operation successful")