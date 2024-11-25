# Write a program that takes a character as input and determines whether it is a vowel or a consonant.

char = input('Enter Your Character : ')
char=char.lower().strip()

vowels=['a' , 'e' , 'i' , 'o' ,'u']
if char in vowels :
    print(f"This Character {char} is a vowel")

else:
    print(f'This Character {char} is a Consonant')