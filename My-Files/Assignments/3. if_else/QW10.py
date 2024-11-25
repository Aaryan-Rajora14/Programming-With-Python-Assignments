# Write a program that calculates the income tax based on the following slabs:
'''Income <= 10,000: No tax
10,001 <= Income <= 20,000: 10% tax
20,001 <= Income <= 50,000: 20% tax
Income > 50,000: 30% tax
'''

y = int(input("Enter Your Income : "))


if y<=10000:
    print("Tax Is NIL")
elif y>=10000 and y<=20000:
    print(f"Total Tax on Income {y} is {(y/100)*10}")
elif y>=20001 and y<=50000:
    print(f"Total Tax on Income {y} is {(y/100)*20}")
elif y>50000:
    print(f"Total Tax on Income {y} is {(y/100)*30}")
else:
    print("Enter Correct Income")    
