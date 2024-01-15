def containerWithMostWater(array):
    mostWater = 0
    left = 0
    right = len(array) - 1
    while left < right:
        height = min(array[left],array[right])
        width = right - left
        currentWater = height * width
        
        if currentWater > mostWater:
            mostWater = currentWater
            
        if array[left] < array[right]:
            left = left + 1
        else:
            right = right - 1
            
    return mostWater

print(containerWithMostWater([1,8,6,2,5,4,8,3,7]))