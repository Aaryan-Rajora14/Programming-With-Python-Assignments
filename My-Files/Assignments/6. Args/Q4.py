# 4.Filter and Apply Function ( Try is questions, if not able to do then we will see the solution for the same in the class )
# Write a function that takes a function and a variable number of arguments, filters out non-numeric values, and applies the function to the remaining arguments.
# Use Case: This is useful in a machine learning or data processing project, where you might need to clean input data and apply transformations.
# Python code
# def filter_and_apply(func, *args): 
# # Your code here

def Filter(func,*args):
    l =[]
    for ele in args:
        if type(ele)==int:
            l.append(ele)

    return func(l)

a = Filter(sum, 100,'pooja',134 ,123 ,153 ,'barkha',200,'Aryan',300 ,120 ,'Twinkle')
print(a)

