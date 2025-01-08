# 1.Write a function that accepts a variable number of numeric arguments and returns their sum.
# Use Case: This function could be used in a financial application where the total cost of multiple items needs to be calculated.

def total_cost(*args):
    return sum(args)

total = total_cost(100, 200, 300, 400)
print(f"The total cost is {total}")
