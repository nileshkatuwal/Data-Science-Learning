# Write a Python program to find the largest of three numbers.

def findlargest(num1,num2,num3):
    if (num1 >= num2 and num1 >= num3):
        print(f'The largest number is {num1}.')
    
    elif (num2 >= num1 and num2 >= num3):
        print(f'The largest number is {num2}.')

    else:
        print(f'The largest number is {num3}.')

findlargest(35, 15, 25)

# Write a Python program to check if a given year is a leap year.

def find_leapyear(year):
    if (year % 400 == 0 and  year % 100 == 0):
        print(f'{year} is a leap year.')

    elif (year % 4 == 0 and year % 100 != 0):
        print(f'{year} is a leap year.')

    else:
        print(f'{year} is not a leap year.')

find_leapyear(2012)

# Write a Python program to determine if a given character is a vowel or a consonant.

vowel = ['a', 'e', 'i', 'o', 'u']

def finder(string):
    if string in vowel:
        print(f'{string} is vowel.')
    
    else:
        print(f'{string} is consonant.')

finder('b')
finder('u')

'''
Outputs:
The largest number is 35.
2012 is a leap year.
b is consonant.
u is vowel.
'''