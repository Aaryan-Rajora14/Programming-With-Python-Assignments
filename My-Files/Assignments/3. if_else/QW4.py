# Write a program that determines if a person can participate in an athletic event based on their age and qualification levels. The criteria are:

'''
1. Age between 18 and 35 and a qualification level of "expert".
2. Age between 36 and 50 and a qualification level of "intermediate" or "expert".
3. Age above 50 and a qualification level of "beginner" or "intermediate" or "expert".
'''

while True:
    age=int(input("Enter Your Age: "))
    q=input('Enter Your Qualification [Beginner, Intermediate, Expert]: ')
    q=q.upper().strip()
    
    if age>=18 and age<35 and q=="EXPERT":
        print(f'At this Age of {age} with Qualification {q} You Can Participate')
    elif age>=36 and age<50 and q=="EXPERT" or q=="INTERMEDIATE":
        print(f'At this Age of {age} with Qualification {q} You Can Participate')
    elif age>30 and q=="EXPERT" or q=="INTERMEDIATE" or q=="BEGINNER":
        print(f'At this Age of {age} with Qualification {q} You Can Participate')
    else:
        print(f"You cannot Participate with qualification {q} at the age of {age}")