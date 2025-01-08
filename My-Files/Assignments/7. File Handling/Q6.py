# 6.	Count Lines in a File: Write a program that counts the number of lines in a file named lines.txt.

with open('Lines.txt','r') as f:
    a = f.readlines()
    print(len(a))