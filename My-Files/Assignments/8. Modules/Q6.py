# 6.	Write a program that takes a year and a month as input and prints the calendar for that month.

def Calen(y):
    import calendar as cal 
    for i in range(1,13):
        a=cal.month(y, i)
        print(a)

while True:
    year = int(input('Enter Year: '))
    Calen(year)