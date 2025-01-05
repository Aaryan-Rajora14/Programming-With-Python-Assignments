# 2. Define a function power_of_number that calculates the power of a given number. The default exponent should be 2.

def power_of_number(n, m=2):
    p = n**m
    return p

while True:
    try:
        n = int(input("Enter Number:"))
    except:
        print("Alphanumberic Values Cant Be Accepted")
    try:
        m = int(input("Enter Exponent:"))
    except:
        m=2
    rt = power_of_number(n, m)
    print(f"The Power of Number {n} with Expnent {m} is {rt}")