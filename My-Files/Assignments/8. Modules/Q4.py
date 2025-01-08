# 4.	Write a program that calculates the user's age in years, months, and days given their date of birth

from datetime import date

def life_lived():

    birthdate=date(year,month,day)
    today=date.today()
    days_lived=(today-birthdate).days

    years_lived=days_lived//365
    monthslived=(days_lived%365)//30
    daysremaining=(days_lived%365)%30
    hourslived=days_lived*24
    minutes=hourslived*60
    seconds=minutes*60
    
    print(f'''\nYou have lived for {years_lived} years,{monthslived} months and {daysremaining} days
Total no of days lived {days_lived}
Total no of hours lived {hourslived}
Total no of minutes lived {minutes}
Total no of seconds lived {seconds} 
till {today}\n''')

while True:
    year=int(input('Enter Birth Year : '))
    month=int(input('Enter Birth Month : '))
    day=int(input('Enter Birth Date : '))
    life_lived()