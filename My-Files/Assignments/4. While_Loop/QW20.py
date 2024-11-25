# 20. Take integer inputs from user until he/she presses q (Ask to press q to quit after every integer input). Print average and product of all numbers.

count = 0
sum = 0
product = 1

while True:
    num = input("Enter an integer (or press 'q' to quit): ")
    
    if num == 'q':
        break
        
    num = int(num)
    count += 1
    sum += num
    product *= num

if count == 0:
    print("No numbers entered.")
else:
    average = sum / count
    print("Average:", average)
    print("Product:", product)
