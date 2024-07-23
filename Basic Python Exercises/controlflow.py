# Write a Python program to print the first 10 natural numbers using a while loop.
number = 1

while (number < 11):
    print (number)
    number += 1 


# Write a Python program to print the multiplication table of a given number using a for loop.
def multiplication_table(num):
    for i in range(1,11):
        print (f'{num} * {i} = {num * i}')

multiplication_table(3)

# Write a Python program to find the sum of all numbers from 1 to 100 using a for loop.
sum = 0
for num in range(1,101):
    sum += num

print (sum)

# Write a Python program to count the number of digits in a given number using a while loop.


def countnum(num):
    count = 0

    if num == 0:
        return 1

    while (num != 0):
        num //= 10
        count += 1
    return count

print(countnum(0))

#Write a Python program to print the Fibonacci sequence up to n terms where n is a user input.


def fibonacci_sum(num):
    fib1, fib2 = 0, 1
    count = 0
    
    if num <= 0:
        print("Please enter a positive integer")
    elif num == 1:
        print("Fibonacci sequence up to", num, ":")
        print(fib1)
    else:
        while count < num:
            print(fib1, end=' ')
            sum1 = fib1 + fib2
            fib1 = fib2
            fib2 = sum1
            count += 1

n = int(input('Enter Number of terms: '))
fibonacci_sum(n)

'''
Outputs:
1
2
3
4
5
6
7
8
9
10
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
3 * 10 = 30
5050
1
Enter Number of terms: 10
0 1 1 2 3 5 8 13 21 34 
'''






