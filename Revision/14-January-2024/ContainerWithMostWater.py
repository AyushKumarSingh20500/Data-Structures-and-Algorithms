def containerWithMostWater(array):
    left = 0
    right = len(array) - 1
    mostCapacity = 0
    while left < right:
        height = min(array[left],array[right])
        width = right - left
        
        currentCapacity = height * width
        if currentCapacity > mostCapacity:
            mostCapacity = currentCapacity
            
        if array[left] < array[right]:
            left = left + 1
        else:
            right = right - 1
            
    return mostCapacity

print(containerWithMostWater([1,8,6,2,5,4,8,3,7]))