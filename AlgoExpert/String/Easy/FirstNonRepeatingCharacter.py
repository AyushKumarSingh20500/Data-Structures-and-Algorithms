# # Time: O(n**2) | Space: O(1)
# def firstNonRepeatingCharacter(string):
#     for idx in range(len(string)):
#         for jdx in range(len(string)):
#             if(jdx != idx and string[jdx] == string[idx]):
#                 break
#         else:
#             return idx
        
#     return -1

# print(firstNonRepeatingCharacter("abcdcaf"))

# -------------------------------------

# Time: O(n), n = length of string | Space: O(1), we can have atmost 26 characters in lookup, which is constant. Size of lookup is not increasing with input.
def firstNonRepeatingCharacter(string):
    lookup = {}
    for char in string:
        if char in lookup.keys():
            lookup[char] += 1
        else:
            lookup[char] = 1
            
    for idx in range(len(string)):
        if(lookup[string[idx]] == 1):
            return idx
        
    return -1

print(firstNonRepeatingCharacter("abcdcaf"))

# by me, without looking