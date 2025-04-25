# 3. Write a program that takes a list of numbers and prints the number at a user-specified index. Use exception handling to manage the case where the user enters an index that is out of range.

while True:                
    numbers_input = input("Enter a list of numbers separated by spaces: ")
    numbers = list(map(int, numbers_input.split(",")))

    try:
        index = int(input("Enter the index of the number you want to retrieve: "))
        try:
            number = numbers[index]
            print(f"The number at index {index} is: {number}")
        except IndexError:
            print(f"Error: Index {index} is out of range for the list.")
    except ValueError:
        print("Error: Please enter a valid integer index.")