# def naturalsum(n):
#     s = 0
#     for i in range(n,0,-1):
#         s += i
#     return s
# print(naturalsum(5))
# print(naturalsum(10))

#Recursive Approach
# def natural_sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + natural_sum(n-1)
# print(natural_sum(5))
# print(natural_sum(10))

#Factorial
# def factorial(n):
#     if n < 0:
#         return "Factorial does not exist for -ve"
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))
# print(factorial(4))


# Fibonacci Series upto n terms
# 0 1 1 2 3...
# def fibonacci(n):
#     if n <= 0:
#         return n
#     elif n == 2:
#         return 1
#     elif n == 1:
#         return 1
#     elif n == 1:
#         return 0
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(5))

# GCD of two numbers
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
print(gcd(4,10))
















