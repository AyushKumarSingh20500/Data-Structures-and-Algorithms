def containerWithMostWater(array):
    left = 0
    right = len(array) - 1
    maxWater = 0
    while left < right:
        height = min(array[left],array[right])
        width = right - left
        currentWater = height * width
        maxWater = max(maxWater,currentWater)
        
        if array[left] < array[right]:
            left = left + 1
        else:
            right = right - 1
            
    return maxWater

print(containerWithMostWater([1,8,6,2,5,4,8,3,7]))
