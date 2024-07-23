# Write a Python program to declare variables of different data types: an integer, a float, a string, and a boolean. Print each variable.
integer = 5
floating_number = 10.5
string = "Python Basics"
booldef = True

print(integer)
print(floating_number)
print(string)
print(booldef)

# Write a Python program to perform addition, subtraction, multiplication, and division operations on two given numbers and print the results.

def add(x,y):
    sum = x + y
    return sum

def subtract(x,y):
    diff = x - y
    return diff

def multiply(x,y):
    result = x * y
    return result

def devide(x,y):
    result = x / y
    return result

print(add(5,3))
print(subtract(5,3))
print(multiply(5,3))
print(devide(5,3))

# Write a Python program to swap the values of two variables without using a temporary variable.
x = 5
y = 6

x, y = y, x
print(x,y)

# Write a Python program to calculate the area of a rectangle given its length and width.

def area_of_rectangle(length, breadth):
    area = length * breadth
    return area

print(area_of_rectangle(5,6))

# Write a Python program to concatenate two strings and print the result.
string1 = "Python"
string2 = "Basics"

newstring = string1 + string2
print(newstring)

# Write a Python program to check if a number is even or odd.
num = 11

if num%2 ==0:
    print("The given number is even.")

else:
    print("The given number is odd.")

'''
Outputs:
5
10.5
Python Basics
True
8
2
15
1.6666666666666667
6 5
30
PythonBasics
The given number is odd.
'''




