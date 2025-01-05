# 6.  write a function returns the highest value among 3 numbers passed as argument

def max_integer():
    maxnum=[]
    while True:
        num = input('Enter Numbers Seaperated By Commas:')
        newnum = list(map(int, num.split(',')))
        if not num:
            break
        maxnum.extend(newnum)
        a = max(maxnum)
        print(f"The Sum of Integers in the list is {a}")

max_integer()