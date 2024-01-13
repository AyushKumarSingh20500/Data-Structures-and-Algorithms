def moveElementToEnd(array,target):
    left = 0
    right = len(array) - 1
    while left < right:
        while array[right] == target:
            right = right - 1
            
        if array[left] == target and left < right:
            array[left],array[right] = array[right],array[left]
            right = right - 1
        left = left + 1
        
    return array

print(moveElementToEnd([2,2,1,1,2,1,2],2))
print(moveElementToEnd([1,2,3,2,1,4,3,1,1,5,1,7,1,8,9,9],1))
print(moveElementToEnd([2,1,2,2,2,3,4,2],2))