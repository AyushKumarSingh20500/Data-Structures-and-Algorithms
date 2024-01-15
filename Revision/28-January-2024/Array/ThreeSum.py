def threeSum(array,target):
    array.sort()
    result = []
    for idx in range(len(array)-2):
        left = idx + 1
        right = len(array) - 1
        while left < right:
            if array[idx] + array[left] + array[right] < target:
                left = left + 1
            elif array[idx] + array[left] + array[right] > target:
                right = right - 1
            else:
                result.append([array[idx],array[left],array[right]])
                left = left + 1
                right = right - 1
                
    return result

print(threeSum([12,3,1,2,-6,5,-8,6], 0))