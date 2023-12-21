# Time: O(n**2), where n = length of array | Space: O(n), where n = length of result
def arrayOfProduct(array):
    result = []
    for i in range(len(array)):
        product = 1
        for j in range(len(array)):
            if i == j:
                continue
            else:
                product = product * array[j]
                
        result.append(product)
    
    return result

print(arrayOfProduct([5,1,4,2]))

# ===============================================

# Time: O(n), where n = length of array | Space: O(n), where n = length of result
def arrayOfProduct(array):
    result = []
    product = 1
    for num in array:
        product = product * num
        
    for num in array:
        result.append(product//num)
        
    return result

print(arrayOfProduct([5,1,4,2]))

# ===============================================

# Time: O(n), where n = length of array | Space: O(1)
def arrayOfProduct(array):
    product = 1
    for num in array:
        product = product * num
        
    for idx in range(len(array)):
        array[idx] = product//array[idx]
        
    return array

print(arrayOfProduct([5,1,4,2]))

# Cannot use division to solve this problem

def arrayOfProduct(array):
    result = []
    
    leftProduct = [1] * len(array)
    leftRunningProduct = 1
    for idx in range(len(array)):
        leftProduct[idx] = leftRunningProduct
        leftRunningProduct = leftRunningProduct * array[idx]
        
    rightProduct = [1] * len(array)
    rightRunningProduct = 1
    for idx in reversed(range(len(array))):
        rightProduct[idx] = rightRunningProduct
        rightRunningProduct =  rightRunningProduct * array[idx]
        
    for i in range(len(array)):
        result.append(leftProduct[i]*rightProduct[i])
    return result

print(arrayOfProduct([5,1,4,2]))