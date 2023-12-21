def threeSum(array,target):
    array.sort()
    result = []
    for i in range(len(array)-2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            if array[i] + array[left] + array[right] < target:
                left = left + 1
            elif array[i] + array[left] + array[right] > target:
                right = right - 1
            else:
                result.append([array[i],array[left],array[right]])
                left = left + 1
                right = right - 1
                
    return result

print(threeSum([12,3,1,2,-6,5,-8,6], 0))

# by me, without looking, very good, very proud