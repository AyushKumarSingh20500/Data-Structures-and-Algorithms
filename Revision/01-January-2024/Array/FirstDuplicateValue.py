def firstDuplicateValue(array):
    for num in array:
        index = abs(num) - 1
        if array[index] < 0:
            return abs(num)
        else:
            array[index] *= -1
            
    return -1

print(firstDuplicateValue([5,1,3,2,5,3]))
