# 17. Remove Empty Strings from a List of Strings: Given a list of strings, remove any empty strings from it using a while loop.

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

i = 0
while i < len(list1):
    if list1[i] == "":
        list1.pop(i)
    else:
        i += 1

print(list1)