# Write a Python script that prompts the user for a sentence and extracts a substring from it. Display both the original sentence and the extracted substring.

a = input("Enter a Senetence : ")

p1 = int(input('Enter Start Point of substring: '))
p2 = int(input('Enter End Point of substring: '))

print(a)
print(a[p1:p2])
