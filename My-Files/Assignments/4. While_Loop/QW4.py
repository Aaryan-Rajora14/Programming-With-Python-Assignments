# 4.  Write a program to find the sum of the digits of a number accepted from user

n=int(input("Enter A NUmber: "))
s=0
while n>0:
    s+=n%10
    n = n//10

print(s)