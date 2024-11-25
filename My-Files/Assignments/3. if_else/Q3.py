# 3. Write a program in python to find out whether a year entered through keyboard is leap year or not.

year = int(input('Enter Year: '))

if year%4==0 and (year%100!=0 or year%400 == 0):
    print(f"This {year} is a leap year")
else:
    print(f"The {year} is not a leap year")