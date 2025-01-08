# 5.	Write a program that creates a new directory, creates a new file within that directory, writes some text to the file, and then reads and prints the content of the file

import os 
if not os.path.exists(r"D:\Machine Learning With Python\My-Files\Assignments\6. Modules\Q5"):
    os.mkdir(r"D:\Machine Learning With Python\My-Files\Assignments\6. Modules\Q5")

else:
    with open(r"D:\Machine Learning With Python\My-Files\Assignments\6. Modules\Q5\New File.txt",'w') as f:
        a = f.write("New File was creared with a new directory in Assignments named as Q5")
        f.close()
        print("File Created Successfully")
    
    with open(r"D:\Machine Learning With Python\My-Files\Assignments\6. Modules\Q5\New File.txt",'r') as f:
        b = f.read()
        print(b)
        f.close()