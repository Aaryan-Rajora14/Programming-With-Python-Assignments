#1.	Write a program that reads a file named data.txt line by line and prints each line.

f = open("data.txt",'w')
a = f.write("""Device name	DESKTOP-70DLJ7G
Processor	Intel(R) Core(TM) i3-7020U CPU @ 2.30GHz   2.30 GHz
Installed RAM	12.0 GB (11.9 GB usable)
Device ID	AC187BBE-C5D6-44EA-B209-BFD18182DAB8
Product ID	00327-35108-38545-AAOEM
System type	64-bit operating system, x64-based processor
Pen and touch	No pen or touch input is available for this display
""")

f.close()

f = open("data.txt",'r')
b = f.read()
print(b)

f.close()