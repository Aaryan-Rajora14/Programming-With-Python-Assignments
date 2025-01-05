# 7.  write a function to display of table of given number.

def tables(n):
    for i in range(1,11):
        a = (f'{n} X {i} = {n*i}\n')
        print(a)
        
n = int(input('Enter Your Number: '))
tables(n)

