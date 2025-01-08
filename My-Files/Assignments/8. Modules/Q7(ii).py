# 7.	Write a program that takes a list of numbers and calculates the mean, median, and mode.

import statistics as st 
while True:
    a = list(map(int, input("Enter Your Numbers: ").split(",")))
    ch = int(input('Select Your Choice 1 for MODE 2 for MEDIAN 3 for MEAN: '))
    if ch == 1:
        b = st.mode(a)
        print(f"The MODE of data is {b}")
    elif ch == 2:
        b = st.median(a)
        print(f"The MEDIAN of data is {b}")
    elif ch == 3:
        b = st.mean(a)
        print(f"The MEAN of data is {b}")
    else:
        print("Thanks for Using the Prgram")