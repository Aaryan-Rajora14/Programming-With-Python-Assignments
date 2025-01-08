# 3.	Write a program that simulates a lottery draw. The program should randomly select 6 distinct numbers between 1 and 49, and display them in ascending order

def lucky_draw():
    import random 
    lst=[]
    i = 0
    while i != 6: 
        a = random.randint(1, 49)
        lst.append(a)
        i+=1

        lst.sort()
    print(f"The Lucky Winners are {lst}")
    
lucky_draw()