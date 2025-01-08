# 2.	Write a program that appends a user-provided string to a file named data.txt.

def addit():
    with open('data.txt','a') as f:
        a = input('Type Here:')
        f.write(f'{a}\n')
        f. close()

def readit():
    with open('data.txt','r') as f:    
        print(f.read())
    
while True:
    ch = input('\nChoose R to read File and A to Add Content :').lower().strip()
    if ch == 'a':
        addit()
    elif ch == 'r':
        readit()