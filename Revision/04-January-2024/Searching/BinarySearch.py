def binarySearch(array,target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right)//2
        if array[middle] < target:
            left = middle + 1
        elif array[middle] > target:
            right = middle - 1
        else:
            return middle
        
    return -1 

print(binarySearch([0,1,21,33,45,45,61.71,72,73],21))