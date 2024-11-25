# 3.grade the student according to marks\

'''•	above 90 (A+)
•	81 to 90 (A)
•	71 to 80 (B+)
•	61 to 70 (B)
•	51 to 60 (C)
•	41 to 50 (D)
•	less than 40 (Fail)
'''
while True:
    m = int(input("Enter Your Marks:"))
    
    if m>=90:
        print(f"Your Grade is A+ with {m} Percent")
    elif m>=81 and m<90:
        print(f"Your Grade is A with {m} Percent")
    elif m>=71 and m<80:
        print(f"Your Grade is B+ with {m} Percent")
    elif m>=61 and m<70:
        print(f"Your Grade is B with {m} Percent")
    elif m>=51 and m<60:
        print(f"Your Grade is C with {m} Percent")
    elif m>=41 and m<50:
        print(f"Your Grade is D with {m} Percent")
    else:
        print(F"You Failed with only {m} Percent")