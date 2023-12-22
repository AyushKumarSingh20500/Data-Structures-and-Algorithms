def containerWithMostWater(array):
    max_water = 0
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] < array[right]:
            height = min(array[left],array[right])
            width = right - left
            current_water = height * width
            left = left + 1
        elif array[left] > array[right]:
            height = min(array[left],array[right])
            width = right - left
            current_water = height * width
            right = right - 1
        else:
            height = min(array[left],array[right])
            width = right - left
            current_water = height * width
            right = right - 1
            
        max_water = max(max_water,current_water)
        
    return max_water

print(containerWithMostWater([1,8,6,2,5,4,8,3,7]))

# by me, without looking, very good, very proud
# did not even watched theoratical solution