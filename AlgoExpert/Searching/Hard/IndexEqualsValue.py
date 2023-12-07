# Time: O(logn) | Space: O(1)
def indexEqualsValue(array):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        # if array[mid] > mid:
        #     right = mid - 1
        # elif array[mid] < mid:
        #     left = mid + 1
        # else:
        #     if mid == 0:
        #         return mid
        #     elif array[mid - 1] < mid - 1:
        #         return mid
        
        if array[mid] < mid:
            left = mid + 1
        elif array[mid] == mid and mid == 0:
            return mid
        elif array[mid] == mid and array[mid - 1] < mid - 1:
            return mid
        else:
            right = mid - 1
    return -1

print(indexEqualsValue([-2,0,2,3,6,8,10]))