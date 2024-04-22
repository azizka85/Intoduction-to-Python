def fib(n):    
    a, b = 0, 1

    while a < n:
        print(a, end=' ')

        a, b = b, a+b

    print()

def fib2(n):
    result = []
    a, b = 0, 1

    while a < n:
        result.append(a)

        a, b = b, a+b
        
    return result

def fib3(n: int, p: int, t: int):
    print(n, end=' ')

    if n == 0:
        fib3(1, 0, t)
    elif n == 1:
        fib3(1 + p, 1, t)
    elif n + p < t:
        fib3(n + p, n, t)
