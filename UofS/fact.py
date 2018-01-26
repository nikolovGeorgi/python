def factorial(n):
    '''
    Purpose:
        Calculate the factorial of a non-negative integer
    Pre-conditions:
        n: non-negative integer
    Return:
        a non-negative integer
    '''
    prod = 1
    while n >= 1:
        prod = prod * n
        n = n - 1
    return prod