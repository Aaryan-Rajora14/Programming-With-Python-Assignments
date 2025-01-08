# 4.	Write a program that reads a file named article.txt and counts the number of words in the file.

f = open('Articles.TXT','r')
a = f.read()
b = a.split()
c=len(b)
print(c)
f.close()