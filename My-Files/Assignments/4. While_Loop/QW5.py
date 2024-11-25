# 5. write a program to print table of a number accepted from user

while True:
    n = int(input("\nEnter A Number T print its table: "))
    m = int(input("\nEnter Your Tables ending Multiple: "))
    for i in range(1,m+1):
        print(f"{n} X {i} = {n*i}")