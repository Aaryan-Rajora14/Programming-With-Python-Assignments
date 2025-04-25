# 8. Write a program that asks the user for a number, converts it to an integer, and prints it. Use exception handling to manage invalid input and include a finally block that prints "End of program" regardless of whether an exception occurred.

while True:
    try:
        a = int(input('Enter a Number: '))
        print(f"Your Number is {a}")
    except Exception as e:
        print(f'ERROR OCCURED:-{e}')
    
    
    finally:
        print('End Of Program')