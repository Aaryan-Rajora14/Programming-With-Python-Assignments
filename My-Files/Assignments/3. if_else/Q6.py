# Write a program that converts temperatures between Celsius and Fahrenheit. Ask the user for the temperature and the unit, and then perform the conversion.

ch = input("Enter Temperature Unit C for Celsius and F for Fahrenheit: ")
ch=ch.upper().strip()

if ch=="F":
    num1=int(input("Enter Temperature in Celcius: "))
    print(f"The {num1} Degree Celcius is {(num1*9/5)+32} Fahrenheit")
    
elif ch=="C":
    num2=int(input("Enter Temperature in Fahrenheit: "))
    print(f"The {num2} Degree Fahrenheit is {(num2 - 32)*5/9} Celcius")

else:
    print("Enter Valid Units")