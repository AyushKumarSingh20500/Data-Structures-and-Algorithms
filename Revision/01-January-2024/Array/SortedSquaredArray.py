def sortedSquaredArray(array):
    result = [0] * len(array)
    left = 0
    right = len(array) - 1
    idx = -1
    while left <= right:
        if abs(array[left]) > abs(array[right]):
            result[idx] = array[left]**2
            left = left + 1
            idx = idx - 1
        elif abs(array[left]) < abs(array[right]):
            result[idx] =  array[right]**2
            right = right - 1
            idx = idx - 1
        else:
            result[idx] = array[right]**2
            left = left + 1
            right = right - 1
            idx = idx - 1
            
    return result

print(sortedSquaredArray([-4,-2,0,1,3]))