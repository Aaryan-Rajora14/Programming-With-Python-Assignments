# 5. Create a simple calculator program that performs addition, subtraction, multiplication, or division based on user input.

ch = input('Enter Your Choice out of + - X / %: ')

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

if ch == '+':
    print(f"Sum of {num1} and {num2} is {num1+num2}")

elif ch == '-':
    print(f"Difference Between {num1} and {num2} is {num1-num2}")

elif ch == 'X':
    print(f"Multiplication of  {num1} and {num2} is {num1*num2}")

elif ch == '/':
    print(f"{num1} Divided by {num2} is {num1/num2}")
    
elif ch == '%':
    print(f"Remainder after {num1} divided by {num2} is {num1%num2}")
    
else:
    print('Enter Valid Choices')