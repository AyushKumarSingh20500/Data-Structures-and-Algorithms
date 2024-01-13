def firstDuplicteValue(array):
    for num in array:
        index = abs(num) - 1
        if array[index] < 0:
            return abs(num)
        else:
            array[index] = array[index] * -1
            
    return -1

print(firstDuplicteValue([2,1,5,2,3,3,4]))