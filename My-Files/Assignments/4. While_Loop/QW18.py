# 18. Print the following patterns using loop :
# a.
# *
# **
# ***
# ****

for i in range(1, 5):
    print('*' * i)
    
# b.
#    *  
#  *** 
# *****
#  *** 
#    *

i=1
j=4
while i <=5:
    print(" "*j,"*"*i)
    i +=2
    j -=1
    
while i >=1:
    print(" "*j,"*"*i)
    i -=2
    j +=1
    
# c.
# 1010101
#  10101 
#   101  
#    1   

k=0
for i in range(7, 0,-2):
    print(" "*k,end=0)
    for j in range(i):
        if j%2==0:
            print(1, end="")
        else:
            print(0, end="")
    
    k+=1
    print("")