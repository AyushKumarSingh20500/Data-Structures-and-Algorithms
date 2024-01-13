def twoSum(array,target):
    array.sort()
    left = 0
    right = len(array) - 1
    result = []
    while left < right:
        if array[left] + array[right] < target:
            left = left + 1
        elif array[left] + array[right] > target:
            right = right - 1
        else:
            result.append([array[left],array[right]])
            left = left + 1
            right = right - 1
            
    return result

print(twoSum([3,5,-4,8,11,1,-1,6], 10))
