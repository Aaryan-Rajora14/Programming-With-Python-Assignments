# 6. Accept 10 numbers from the user and display their average

while True:
    total = 0
    for i in range(10):
        number = float(input(f"Enter number {i+1}: "))
        total += number
        
    average = total / 10
    print(f"The average of the entered numbers is: {average}")