# def firstNonRepeatingCharacter(string):
#     for i in range(len(string)):
#         for j in range(len(string)):
#             if i != j and string[i] == string[j]:
#                 break
#         else:
#             return i
        
#     return -1

# print(firstNonRepeatingCharacter("abcdcaf"))

def firstNonRepeatingCharacter(string):
    lookup = {}
    for char in string:
        if char in lookup:
            lookup[char] += 1
        else:
            lookup[char] = 1
            
    for idx in range(len(string)):
        if lookup[string[idx]] == 1:
            return idx
        
    return -1

print(firstNonRepeatingCharacter("abcdcaf"))