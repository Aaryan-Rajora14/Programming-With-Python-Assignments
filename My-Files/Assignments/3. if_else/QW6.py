# Write a program that determines if a triangle is valid and, if so, categorizes it as:

'''Equilateral (All sides are equal)
Isosceles (2 sides are equal)
Scalene (All sides are different)

Invalid (if the sides do not form a triangle): condition for triangle formation 
for given 3 sides(a,b,c) is sum of any 2 sides should be greater than 3rd side.
'''
while True:
    a=int(input("Enter Side a Of Triangle: "))
    b=int(input("Enter Side b Of Triangle: "))
    c=int(input("Enter Side c Of Triangle: "))

    if a+b>c or b+c>a or a+c>b:
        if a== b == c:
            print("The Triangle is Equilateral Triangle")
            
        elif a==b or a==c or b==c:
            print("Your Triangle is Isoceles Triangle")

        elif a+b<c or b+c<a or a+c<b:
            print("Your Sides Didn't Form A Triangle")

        else:
            print("Your Triangle is a Scalene Triangle")