# 3.	Write a program that prompts the user for a string and writes that string to a file named output.txt.

with open('Output.txt','w') as f:
    a = input('Type your Prompt: ')
    f.write(a)
    print('Your Prompt Successfully Initiated')
    f.close()