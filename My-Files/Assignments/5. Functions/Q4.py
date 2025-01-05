# 4. Create a function reverse_string that reverses a given string. The default string should be “Hello, World!”.

def reverse_string(a='Hello World'):
    return a[::-1]

while True:
    a = input('Enter Your Words:')
    if not a:    
        a = ('Hello World')
    
    c = reverse_string(a)
    print(f"The Reverse of {a} is {c}")