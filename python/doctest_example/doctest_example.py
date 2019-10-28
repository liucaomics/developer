'''
    a function returns n!
    >>> [factorial(i) for i in range(1,5,1)]
    [1, 2, 6, 24]
    
    >>> factorial(0)
    Traceback (most recent call last):
        ...
    ValueError: n must be positive
    
    >>> factorial(1e300)
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "<stdin>", line 19, in factorial
    ValueError: n must be integer

    >>> factorial(1.1)
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "<stdin>", line 19, in factorial
    ValueError: n must be integer
'''
def factorial(n):
    '''
    >>> factorial(5)
    120
    '''
    if n<=0:
        raise ValueError("n must be positive")
    if not isinstance(n,int):
        raise ValueError("n must be integer")
    if n == n+1:
        raise OverflowError("n is too large")
    out = 1
    for i in range(1,n+1,1):
        out *= i
    return out

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest.testfile("test.txt")