# def firstNonRepeatingCharacter(string):
#     for idx in range(len(string)):
#         for jdx in range(len(string)):
#             if idx != jdx and string[idx]==string[jdx]:
#                 break
#         else:
#             return idx
                
#     return -1

# print(firstNonRepeatingCharacter("abcdcaf"))

def firstNonRepeatingCharacter(string):
    frequency = {}
    for char in string:
        if char in frequency.keys():
            frequency[char] = frequency[char] + 1
        else:
            frequency[char] = 1
            
    for idx in range(len(string)):
        if frequency[string[idx]] == 1:
            return idx
        
    return -1

print(firstNonRepeatingCharacter("abacbfdc"))
