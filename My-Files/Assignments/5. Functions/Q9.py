# 9.  write a function to check given number is a prime number or not

def Optimus_Prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


while True:
    n = int(input("Type Your Number: "))
    if Optimus_Prime(n):
        print(f"/n{n} is a prime number.")
    else:
        print(f"/n{n} is a Composite number.")
