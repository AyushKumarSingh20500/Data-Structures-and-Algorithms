def indexEqualsValue(array):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] > mid:
            right = mid - 1
        elif array[mid] < mid:
            left = mid + 1
        else:
            return mid
        
    return -1

print(indexEqualsValue([-2,0,1,2,4,8,10]))
