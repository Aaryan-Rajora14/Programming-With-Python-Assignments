# 9.	Write a program that creates a new directory, creates a new file within that directory, writes some text to the file, and then reads and prints the content of the file.

import os 
dname = input('Name Your Directory to be created:')
if not os.path.exists(dname):
    os.makedirs(dname)
    nf = input('Type Your Filename:')
    f = open(f'{dname}\\{nf}','w')
    a = input('Type Some Text In your File:')
    f.write(a)
    print(a)
    f.close()
else:
    print('Directory Already Exists')