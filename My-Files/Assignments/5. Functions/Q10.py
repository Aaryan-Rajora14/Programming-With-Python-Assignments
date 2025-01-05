# 10. Write a Python function to multiply all the numbers in a list.

def multiply_list():
    while True:
        numbers = input("Enter numbers separated by spaces: ").split()
        numbers = [int(number) for number in numbers]
        result = 1
        for number in numbers:
            result *= number
        return result
    
while True:
    product = multiply_list()
    print(f"\nThe product of the list is: {product}")
