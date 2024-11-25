# 16. Concatenate Two Lists Index-Wise: Given two lists of equal length, create a new list by concatenating elements index-wise.

list1 = ["Badminton", "Hockey", "Racing", "Football", "Cricket"]
list2 = [' Saina', ' Dhanraj', ' Narayana', ' Sunil', ' Dhoni']

list3 = []

for item1, item2 in zip(list1, list2):
    item3 = item1 + item2
    list3.append(item3)

print(list3)