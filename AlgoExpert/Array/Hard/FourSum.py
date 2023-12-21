def fourSum(array,target):
    array.sort()
    result = []
    for i in range(len(array)-3):
        for j in range(i+1,len(array)-2):
            left = j + 1
            right = len(array) - 1
            while left < right:
                if array[i] + array[j] + array[left] + array[right] < target:
                    left = left + 1
                elif array[i] + array[j] + array[left] + array[right] > target:
                    right = right - 1
                else:
                    result.append([array[i],array[j],array[left],array[right]])
                    left = left + 1
                    right = right - 1
                    
    return result

print(fourSum([1,0,-1,-2,2,0],0))

# by me, without looking, very good, very proud