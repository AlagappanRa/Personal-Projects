def new_fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return new_fib(n - 1) + new_fib(n - 2)

print(new_fib(5))
