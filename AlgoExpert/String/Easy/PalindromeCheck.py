# # Time: O(n**2), n = length of string | Space: O(n), n = length of reversedString
# def palindromeCheck(string):
#     reversedString = ""
#     for char in reversed(string):
#         reversedString += char
        
#     return string == reversedString
    
# print(palindromeCheck("madam"))

# ---------------------------------------

# # Time: O(n), n = length of string | Space: O(n), n = length of reversedString
# def palindromeCheck(string):
#     reversedString = []
#     for char in reversed(string):
#         reversedString.append(char)
        
#     return string == "".join(reversedString)

# print(palindromeCheck("madam"))

# -------------------------------------

# Time: O(n), n = length of string | Space: O(1)
def palindromeCheck(string):
    left = 0
    right = len(string) - 1
    while left <= right:
        if(string[left] == string[right]):
            left += 1
            right -= 1
        else:
            return False
        
    return True

print(palindromeCheck("madam"))

# by me, without looking

# -------------------------------------

# # Time: O(n) | Space: O(n)
# def palindromeCheckRecursive(string,idx=0):
#     jdx = len(string) - 1 - idx
#     if idx >= jdx:
#         return True
#     else:
#         return string[idx] == string[jdx] and palindromeCheckRecursive(string,idx+1)
    
# print(palindromeCheckRecursive("madam"))

# # looked code, revise it