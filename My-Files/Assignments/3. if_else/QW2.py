# 2.Write a program to classify a person's body mass index (BMI) based on their weight and height. The classification is:

'''
Underweight: BMI < 18.5
Normal weight: 18.5 <= BMI < 24.9
Overweight: 24.9 <= BMI < 29.9
Obesity: BMI >= 30
'''

a=0
while a == 0: 
    w = int(input("\nEnter Your Weight In KGs: "))
    h = int(input("Enter Your Height In CMs: "))

    h2 = h/100
    bmi = w/(h2*h2)

    if bmi<18.5:
        print(f"\nYour BMI is {bmi} Underweigth")

    elif bmi>=18.5 and bmi<=24.9:
        print(f"\nYour BMI is {bmi} Normal Weight")

    elif bmi>=24.9 and bmi<=29:
        print(f"\nYour BMI is {bmi} Overweight")
    
    else:
        print(f"\nYour BMI is {bmi} Overweight")