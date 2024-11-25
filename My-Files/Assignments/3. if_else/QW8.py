# Write a program that categorizes a given year as:
'''Leap Year (divisible by 400 or divisible by 4 but not by 100)
Century Year (divisible by 100 but not by 400)
Common Year (all other years)
'''
while True:
    year = int(input('Enter Year: '))

    if year%4==0 and (year%100!=0 or year%400 == 0):
        print(f"This {year} is a leap year")
    elif year%100==0 and year%400!=0:
        print(f"The year {year} is a Century year but not a Leap Year")
    else:
        print(f"The year {year} is a Common Year")