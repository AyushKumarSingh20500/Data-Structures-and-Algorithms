# Time: O(n**2), n = length of array | Space: O(n), n = length of result array
# def arrayOfProduct(arr):
#     result = []
#     for i in range(len(arr)):
#         total = 1
#         for j in range(len(arr)):
#             if(j != i):
#                 total = total * arr[j]
                
#         result.append(total)
        
#     return result

# print(arrayOfProduct([5,1,4,2]))

# print(arrayOfProduct([4,4]))

# by me, without looking

# --------------------------------------------------

# Time: O(n), n = length of array | Space: O(n), n = length of array
def arrayOfProduct(arr):
    leftProductArray = [0] * len(arr)
    rightProductArray = [0] * len(arr)
    result = [0] * len(arr)
    leftProduct = 1
    rightProduct = 1
    
    for i in range(len(arr)):
        leftProductArray[i] = leftProduct
        leftProduct = leftProduct * arr[i]
        
    for i in reversed(range(len(arr))):
        rightProductArray[i] = rightProduct
        rightProduct = rightProduct * arr[i]
        
    for i in range(len(arr)):
        result[i] = leftProductArray[i] * rightProductArray[i]
        
    return result

print(arrayOfProduct([5,1,4,2]))

# by me, without looking