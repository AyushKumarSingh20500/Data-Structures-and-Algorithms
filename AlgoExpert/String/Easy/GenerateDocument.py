# # Time: O(n * (n + m)), n = length of document and m = length of characters | Space: O(1)
# def generateDocument(characters,document):
#     for char in document:
#         needed = document.count(char)
#         if(characters.count(char) < needed):
#             return False
#         else:
#             continue
        
#     return True

# print(generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))

# ---------------------------------------

# # Time: O(c * (n + m)), c = number of unique characters in document, n = length of document and m = length of characters | Space: O(n), n = length of counted array
# def generateDocument(characters,document):
#     counted = []
#     for char in document:
#         if char not in counted:
#             counted.append(char)
#             needed = document.count(char)
#             if(characters.count(char) < needed):
#                 return False
#             else:
#                 continue
#         else:
#             continue
        
#     return True

# print(generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))

# -------------------------------------

# Time: O(n + m), n = length of characters and m = length of document | Space: O(n), n = length of lookup
def generateDocument(characters,document):
    lookup = {}
    for char in characters:
        if char in lookup.keys():
            lookup[char] += 1
        else:
            lookup[char] = 1
            
    for char in document:
        if char in lookup.keys():
            if lookup[char] > 0:
                lookup[char] -= 1
            else:
                return False
        else:
            return False
        
    return True

print(generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))

# by me, without looking