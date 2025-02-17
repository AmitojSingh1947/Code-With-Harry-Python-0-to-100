import math
# def square(n):
#     # print(n)
#     # '''Takes in a number n, returns the square of n'''
#     # print(n**2)
# square(5)

def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2

print(square.__doc__)

# Recursion Concept 

def factorial(num):
    '''This function will calculate the factorial of a given integer.
    
    The function will take one integer argument, and return the factorial of that number.
    The factorial of a number is the product of all positive integers less than or equal to that number.
    For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.
    '''
#     if(num == 0):
#         return 1
#     else:
#         return num * factorial(num - 1)
# print(factorial(5))

# fibonacci Series 
def fib(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
                    # 2    +   1 = 3
print(fib(2))
print(fib(6))

