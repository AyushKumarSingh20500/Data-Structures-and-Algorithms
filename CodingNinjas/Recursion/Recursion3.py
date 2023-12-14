# def geometricSum(k):
#     if k == 0:
#         return 1
#     else:
#         return geometricSum(k-1) + 1/2**k

# print(geometricSum(3))

# ===================================

# def sumOfDigits(integer):
#     if integer <= 9:
#         return integer
#     else:
#         return integer % 10 + sumOfDigits(integer//10)

# print(sumOfDigits(12345))

# ===================================

# def multiplication(m,n):
#     if n == 1:
#         return m
#     else:
#         return m + multiplication(m,n-1)
    
# print(multiplication(7,7))

# ===================================

# def countZeros(integer):
#     if integer in range(1,10):
#         return 0
    
#     digit = integer % 10
    
#     if digit == 0:
#         return 1 + countZeros(integer//10)
#     else:
#         return countZeros(integer//10)
    
# print(countZeros(1234008))

# ===================================

# def stringToInteger(string,idx=0):
#     if len(string) == idx:
#         return 0
#     else:
#         return int(string[idx]) * (10**len(string[idx+1:])) + stringToInteger(string,idx+1)
    
# print(stringToInteger("12345"))

# ===================================

# def pairStar(string,idx = 0):
#     if len(string) == idx:
#         return ""
    
#     if len(string) - 1 == idx:
#         return string[idx]
    
#     if string[idx] == string[idx+1]:
#         return string[idx] + "*" + pairStar(string,idx+1)
#     else:
#         return string[idx] + pairStar(string,idx+1)
    
# print(pairStar("aaaa"))

# ===================================

# def checkAB(string,idx=0):
#     if len(string) == idx:
#         return True
    
#     if string[idx] == "a" and len(string) - 1 == idx:
#         return True
    
#     if string[idx] == "a":
#         if string[idx+1] == "a":
#             return checkAB(string,idx+1)
#         elif string[idx+1:idx+3] == "bb":
#             return checkAB(string,idx+3)
#         else:
#             return False
#     else:
#         return False
    
# print(checkAB("aabbaabbabb"))

# ===================================

# def staircase(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     elif n == 3:
#         return 4
#     else:
#         return staircase(n-1) + staircase(n-2) + staircase(n-3)
    
# print(staircase(5))