# 21. Write a program that takes a list of tuples representing students' names and scores, and categorizes each student as "Pass" or "Fail" based on a passing score of 50.
# Eg: students = [("Alice", 85), ("Bob", 42), ("Charlie", 59), ("David", 30), ("Eva", 76)]

students = [("Alice", 85), ("Bob", 42), ("Charlie", 59), ("David", 30), ("Eva", 76)]
passed = 50

for student in students:
    name, score = student 
    if score >= passed:
        result = "Pass"
    else:
        result = "Fail"
    
    print(f"{name}: {result}")