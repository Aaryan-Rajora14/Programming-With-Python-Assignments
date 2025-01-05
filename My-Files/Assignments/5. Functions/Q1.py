# 1. Write a function convert_temperature that takes a temperature in Celsius as an argument and converts it to Fahrenheit. The default value for the Celsius temperature should be 0.

def temp1(cel=0):
    fh = ((cel*1.8)+32)
    return fh

def temp2(far):
    cel = ((5/9)*(far-32)) 
    return cel   

while True:
    Ch = input("Enter 'Ch' to convert Celcius into Fahrenheit or 'Fh' to convert Fahrenheit into Celcius:").lower().strip()
    if Ch == 'ch':
        try: 
            a = int(input("Enter Temperature in Celcius :"))
            faren = temp1(a)
            print(f"Temperatur is {faren} Fahrenheit")
        except:
            print("Can't Accept Alphanumeric Values")
    elif Ch == 'fh':
        try:
            b = int(input("Enter Temperature in Fahrenheit:"))
            celsi = temp2(b)
            print(f"Temperature is {celsi} Celcius")
        except:
            print("Can't Accept Alphanumeric Values")
    else:
        print("Please Enter Correct Options")