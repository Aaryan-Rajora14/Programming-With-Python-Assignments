# 1.	Write a program that determines the day of the week based on a given date. The date should be provided in the format YYYY-MM-DD, and the program should validate the input.

def weekday_name(s):
    
    import calendar as cal
    year, month, day = map(int, s.split('-'))
    actual_day = cal.weekday(year, month, day)

    a = cal.day_name[actual_day]
    print(f"The Day on {s} is {a}")

while True:
    date = input("Enter Date in YYYY-MM-DD Format: ")
    weekday_name(date)