# 8.

'''
A
BC
DEF
GHIJ
KLMNO
'''

a = ord('A')
for i in range(1, 6): 
    for j in range(i):
        print(chr(a), end='')
        a += 1
    
    print()