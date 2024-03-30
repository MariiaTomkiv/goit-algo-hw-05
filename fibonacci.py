def caching_fibonacci(n):
    cash = {}
    
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        for n in range(2, n):
            if n in cash:
                return cash[n]
            cash[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cash[n]
    return fibonacci

fib = caching_fibonacci
print(fib(1))