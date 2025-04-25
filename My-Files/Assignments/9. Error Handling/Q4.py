# 4. Write a program that takes a dictionary and asks the user for a key. Print the value associated with that key. Use exception handling to manage the case where the key doesn't exist in the dictionary.

def get_dictionary_from_user():
    dictionary = {}
    print("Enter key-value pairs for the dictionary. Type 'done' to finish.")
    while True:
        key = input("Enter key: ")
        if key.lower() == 'done':
            break
        value = input(f"Enter value for key '{key}': ")
        dictionary[key] = value
    return dictionary
def main():
    user_dict = get_dictionary_from_user()
    key = input("Enter a key to find its value: ")
    
    try:
        value = user_dict[key]
        print(f"The value for key '{key}' is: {value}")
    except KeyError:
        print(f"Key '{key}' does not exist in the dictionary.")



main()