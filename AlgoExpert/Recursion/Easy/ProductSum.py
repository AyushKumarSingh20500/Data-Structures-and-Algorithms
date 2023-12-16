def productSum(array,multiplier):
    result = 0
    for element in array:
        if type(element) == list:
            result = result + productSum(element,multiplier+1)
        else:
            result = result + element
            
    return result * multiplier

print(productSum([5,2,[7,-1],3,[6,[-13,8],4]],1))