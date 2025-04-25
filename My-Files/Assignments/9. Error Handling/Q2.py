# 2. Write a program that asks the user for a number and prints the square of that number. Use exception handling to manage the case where the user enters something that isn't a number.

while True:
    try:
        a = int(input('Enter a Number: '))
        c = a*a
        print(f"The Square of {a} id {c}\n")
    
    except:
        print(f'Only Use Numbers\n')