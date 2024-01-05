def productSum(array, multiplier = 1):
    product = 0
    for item in array:
        if type(item) != list:
            product = product + item
        else:
            product = product + productSum(item, multiplier + 1)
            
    return product * multiplier

print(productSum([5,2,[7,-1],3,[6,[-13,8],4]]))