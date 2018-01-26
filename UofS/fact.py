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
    for i in range (1, n):
        prod = prod * i
    return prod
