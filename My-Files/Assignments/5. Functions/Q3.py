# 3. Write a function sum_integers that computes the sum of a list of integers. If no list is provided, it should return 0.

def sum_integers():
    sumnum=[]
    while True:
        num = input('Enter Numbers Seaperated By Commas:')
        newnum = list(map(int, num.split(',')))
        if not num:
            break
        sumnum.extend(newnum)
        a = sum(sumnum)
        print(f"The Sum of Integers in the list is {a}")

sum_integers()