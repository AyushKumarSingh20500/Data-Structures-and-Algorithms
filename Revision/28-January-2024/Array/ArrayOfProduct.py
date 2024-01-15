# def arrayOfProduct(array):
#     result = []
#     for idx in range(len(array)):
#         product = 1
#         for jdx in range(len(array)):
#             if idx == jdx:
#                 continue
#             else:
#                 product = product * array[jdx]
                
#         result.append(product)
        
#     return result

# print(arrayOfProduct([5,1,4,2]))

def arrayOfProduct(array):
    result = [0] * len(array)
    
    leftProduct = [0] * len(array)
    leftRunningProduct = 1
    for idx in range(len(array)):
        leftProduct[idx] = leftRunningProduct
        leftRunningProduct = leftRunningProduct * array[idx]
        
    rightProduct = [0] * len(array)
    rightRunningProduct = 1
    for idx in reversed(range(len(array))):
        rightProduct[idx] = rightRunningProduct
        rightRunningProduct = rightRunningProduct * array[idx]
        
    for idx in range(len(array)):
        result[idx] = leftProduct[idx] * rightProduct[idx]
        
    return result

print(arrayOfProduct([5,1,4,2]))