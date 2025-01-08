# 2.	Write a program that takes two dates as input and calculates the number of days between them.


def days_difference(d1, d2):
    from datetime import datetime as dt 

    dated1 = dt.strptime(d1, "%Y-%m-%d")
    dated2 = dt.strptime(d2, "%Y-%m-%d")

    no_of_days = abs((dated2-dated1).days)

    print(f"The difference betweeen date {dated1} and {dated1} is {no_of_days}")
    
while True:
    date1 = input('Enter First Date YYYY-MM-DD: ')
    date2 = input('Enter Second Date YYYY-MM-DD: ')
    days_difference(date1, date2)