# Write a program to check if a given time 
# (in 24-hour format,in HH:MM) is in the 
# morning (5 AM to 11:59 AM), 
# afternoon (12 PM to 4:59 PM), 
# evening (5 PM to 8:59 PM), 
# or night (9 PM to 4:59 AM).

while True:
    h, m = map(int, input("Enter Your Time Seaperated by ':' ").split(":"))
    if (h>=5 and m<00) and (h>11 and m<=59):
        print("Morning")
    elif (h>12 and m<=00) and (h>16 and m<=59):
        print("After Noon")
    elif (h>17 and m<=00) and (h>20 and m<=59):
        print("Evening")
    else:
        print("Night")