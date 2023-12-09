# # Factorial - Iterative
# def factorial(n):
#     result = 1
#     for i in range(1,n+1):
#         result = result * i
        
#     return result

# print(factorial(5))

# # Factorial - Recursive
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(6))

# ===================================

# # Sum of first n natural numbers - Iterative
# def sum_1_to_n(n):
#     result = 0
#     for i in range(1,n+1):
#         result = result + i
        
#     return result

# print(sum(5))

# # Sum of first n natural numbers - Recursive
# def sum_1_to_n(n):
#     if n == 1:
#         return 1
#     else:
#         return  n + sum_1_to_n(n-1)
    
# print(sum_1_to_n(5))

# ===================================

# # Power - Iterative
# def power(x,n):
#     result = 1
#     for i in range(n):
#         result = result * x
        
#     return result

# print(power(5,2))

# # Power - Recursive
# def power(x,n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return x
#     else:
#         return x * power(x,n-1)
    
# print(power(3,4))

# ===================================

# # Recursive
# def print_1_to_n(n):
#     if n == 1:
#         print(1)
#     else:
#         print_1_to_n(n-1)
#         print(n)
        
# print_1_to_n(9)

# ===================================

# # Recursive
# def print_n_to_1(n):
#     if n == 1:
#         print(1)
#     else:
#         print(n)
#         print_n_to_1(n-1)
        
# print_n_to_1(9)

# ===================================

