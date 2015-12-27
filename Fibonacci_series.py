def fib(n):
    assert type(n)==int and n >= 0
    if n <= 1:
        return  1
    return fib(n-1)+fib(n-2)
