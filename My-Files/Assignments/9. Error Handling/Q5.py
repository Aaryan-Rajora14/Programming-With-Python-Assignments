# 5. Write a program that opens a file specified by the user and reads its contents. Use exception handling to manage the case where the file doesn't exist.
import os

while True:
    try:
        filename = input("Enter the filename: ")
        f = open(filename, 'r')
        a = f.read()
        print(a)
    except Exception as e:
        print(f"ERROR OCCURED:- {e}")