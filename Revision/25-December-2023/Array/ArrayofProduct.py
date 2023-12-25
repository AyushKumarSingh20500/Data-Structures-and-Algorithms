# def arrayOfProduct(array):
#     result = []
#     for i in range(len(array)):
#         product = 1
#         for j in range(len(array)):
#             if i == j:
#                 continue
#             else:
#                 product = product * array[j]
                
#         result.append(product)
        
#     return result

# print(arrayOfProduct([5,1,4,2]))

# ===============================================

def arrayOfProduct(array):
    result = []
    
    leftProduct = [0] * len(array)
    leftRunningProduct = 1
    for i in range(len(array)):
        leftProduct[i] = leftRunningProduct
        leftRunningProduct = leftRunningProduct * array[i]
        
    rightProduct = [0] * len(array)
    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        rightProduct[i] = rightRunningProduct
        rightRunningProduct = rightRunningProduct * array[i]
        
    for i in range(len(array)):
        result.append(leftProduct[i] * rightProduct[i])
        
    return result

print(arrayOfProduct([5,1,4,2]))