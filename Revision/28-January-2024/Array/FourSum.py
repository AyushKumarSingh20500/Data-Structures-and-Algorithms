def fourSum(array,target):
    array.sort()
    result = []
    for idx in range(len(array)-3):
        for jdx in range(idx+1,len(array)-2):
            left = jdx + 1
            right = len(array) - 1
            while left < right:
                if array[idx] + array[jdx] + array[left] + array[right] < target:
                    left = left + 1
                elif array[idx] + array[jdx] + array[left] + array[right] > target:
                    right = right - 1
                else:
                    result.append([array[idx],array[jdx],array[left],array[right]])
                    left = left + 1
                    right = right - 1
                    
    return result

print(fourSum([1,0,-1,-2,2,0],0))