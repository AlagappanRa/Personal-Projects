def sum_even_factorials(n):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n*factorial(n-1)

    result = 0
    for x in range(n,-1,-2):
        if n %2 != 0:
            n = n-1
        result += factorial(x)
    return result

print(sum_even_factorials(6))

# Space: O(n)
# Time: O(n**2)

'''----------------------------------------'''
def sum_even_fact_improved(n):
    factorial_1 = 1
    result = 1
    for i in range (1,n+1):
        factorial_1 *= i
        if i%2 == 0:
            result += factorial_1
        else:
            continue
    return result

print(sum_even_fact_improved(6))

# Space: O(1)
# Time: O(n)

'''-----------------------------------------'''
