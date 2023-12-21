def twoSum(array,target):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] + array[right] < target:
            left = left + 1
        elif array[left] + array[right] > target:
            right = right - 1
        else:
            return [array[left],array[right]]
        
    return [-1,-1]

print(twoSum([3,5,-4,8,11,1,-1,6],9))