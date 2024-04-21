def caching_fibonacci(n, cache ={}):
    
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
             return 1
        else:
            for n in range(2, n):
                if n in cache:
                    return cache[n]
                else:
                    cache[n] = cache[n-1] + cache[n-2]
        return cache[n]
    
    return fibonacci

fib = caching_fibonacci
print(fib(10))