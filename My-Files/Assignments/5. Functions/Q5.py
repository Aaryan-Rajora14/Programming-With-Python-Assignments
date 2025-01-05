# 5. Create a function greet_user that takes a user’s name as an argument and prints a personalized greeting. If no name is provided, it should greet as “Hello, Guest!”.

def greet_user(n='Guest!', m='Hello'):
    a = m, n 
    return a

while True:
    name = input("Your Name:")
    if not name:
        name = "Guest!"
    
    print(greet_user(name))