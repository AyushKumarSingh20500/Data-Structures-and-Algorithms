def moveElementToEnd(array,target):
    left = 0
    right = len(array) - 1
    while left < right and array[right] == target:
        right = right - 1
        
    while left < right:
        if array[left] == target and array[right] != target:
            array[left], array[right] = array[right], array[left]
            right = right - 1
            left = left + 1
        elif array[left] == target and array[right] == target:
            right = right - 1
        else:
            left = left + 1
        
    return array

print(moveElementToEnd([1,2,3,2,1,4,3,1,1,5,1,7,1,8,9,9],1))