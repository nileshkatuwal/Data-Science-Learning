# Write a Python function to find the factorial of a given number.

def factorial(num):
    if num < 0:
        print("Inavlid Input!! Numbers must be greater than 0")
    
    elif num == 0:
        print("The factorial of 0 is 1.")

    else:
        fact = 1
        for i in range(1, num+1):
            fact = fact * i
        return fact

print(factorial(8))

# Write a Python function that takes a list of numbers as input and returns the maximum number in the list.

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(find_max([1,5,8,4,9]))


# 18. Write a Python function that checks if a given string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]

print("Is 'radar' a palindrome?", is_palindrome("radar"))

# 19. Write a Python function that takes two arguments, a string and a character, and returns the number of times the character appears in the string.

def count_char(s, char):
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count

print("Count of 'l' in 'Hello World':", count_char("Hello World", 'l'))

# 20. Write a Python script that imports the math module and uses its sqrt function to calculate the square root of a given number.

import math

num = 16
print("Square root of", num, "is", math.sqrt(num))

'''
Outputs:
40320
9
Is 'radar' a palindrome? True
Count of 'l' in 'Hello World': 3
Square root of 16 is 4.0
'''