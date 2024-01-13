def arrayOfProduct(array):
    result = []
    
    leftProduct = [0] * len(array)
    leftRunningProduct = 1
    for idx in range(len(array)):
        leftProduct[idx] = leftRunningProduct
        leftRunningProduct = leftRunningProduct * array[idx]
        
    rightProduct = [0] * len(array)
    rightRunningProduct = 1
    for idx in reversed(range(len(array))):
        rightProduct[idx] =  rightRunningProduct
        rightRunningProduct = rightRunningProduct * array[idx]
        
    for idx in range(len(array)):
        result.append(leftProduct[idx] * rightProduct[idx])
        
    return result

print(arrayOfProduct([5,1,4,2]))