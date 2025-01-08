# 2.Write a function that accepts any number of string arguments and concatenates them into a single string, separated by spaces.
# Use Case: This function could be used in a text-processing tool to combine multiple user inputs into a single sentence or paragraph.

def constr(*args):
    return " ". join(args)

a = constr("I","am","Superman")
print(a)