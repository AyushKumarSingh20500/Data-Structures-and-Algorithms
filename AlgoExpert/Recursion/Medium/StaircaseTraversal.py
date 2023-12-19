# # Time: O(k**n), where n = height and k = steps | Space: O(n), where n = height
# def staircaseTraversel(height,steps):
#     if height == 0 or height == 1:
#         return 1
    
#     result = 0
#     for i in range(1,min(height,steps)+1):
#         result = result + staircaseTraversel(height-i,steps)
        
#     return result

# print(staircaseTraversel(4,2))

# =======================================

# # Time: O(n * k), where n = height and k = steps | Space: O(n), where n = height
# def staircaseTraversel(height,steps,memoize = {0:1,1:1}):
#     if height in memoize:
#         return memoize[height]
#     else:
#         result = 0
#         for i in range(1,min(height,steps)+1):
#             result = result + staircaseTraversel(height-i,steps)
#         memoize[height] = result
        
#         return result
    
# print(staircaseTraversel(4,2))

# =======================================

# Time: O(n*k), where n = height and k = steps | Space: O(n), where n = length of result
def staircaseTraversel(height,steps):
    result = [0] * (height + 1)
    
    result[0] = 1
    result[1] = 1
    
    for i in range(2,len(result)):
        ways = 0
        for j in range(1,steps+1):
            ways = ways + result[i-j]
            
        result[i] = ways
        
    return result[height]

print(staircaseTraversel(4,2))