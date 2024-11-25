# Write a program to calculate the fee based on age and membership status. The fee structure is:
'''
Regular members get a 20% discount.
Senior citizens (age > 60) get a 30% discount.
Children (age < 12) get a 50% discount.
Otherwise, the full fee is charged.
'''

while True:
    age= int(input("Enter Your Age :"))
    f = int(input("Enter Fees to be Paid and Apply discount:"))
    m = input("Enter Your Membership Status YES or NO :")
    m = m.upper().strip()

    if age>=13 and age<=59 and m == "YES":
        dsf=f-((f/100*20))
        print(f"As a Member with age {age} You have to pay {dsf} fees")

    elif age>60:
        dsf=f-((f/100*30))
        print(f"As a Senior Citizen with age {age} You have to Pay {dsf} fees")

    elif age<12:
        dsf=f-((f/100*50))
        print(f"As a Childreb with age {age} You have to Pay {dsf} fees")

    else:
        print(f"As a Non member with age {age} You Have to Pay Full Fees {f}")