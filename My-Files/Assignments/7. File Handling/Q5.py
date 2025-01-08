# 5.	Write a program that copies the content of a file named source.txt to a new file named destination.txt.

with open('Source.txt','r') as f:
    a = f.read()
with open('Destination.txt','w') as f1:
    b = f1.write(a)
    f1.close()
with open('Destination.txt','r') as f2:
    c = f2.read()
    print(c)
    f2.close