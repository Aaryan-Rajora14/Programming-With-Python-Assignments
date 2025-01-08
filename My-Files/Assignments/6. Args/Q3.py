# 3.Write a function that accepts any number of numerical arguments and returns the maximum value.
# Use Case: This function can be used in a data analytics project to find the maximum value from a set of dynamically provided data points.

def maxval(*args):
    return max(args)

value = maxval(12,43,12,45,34,78,34,98,3,3245,6754,243,5623,6722)
print(value)