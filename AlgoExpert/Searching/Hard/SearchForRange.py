# Time: O(logn) | Space: O(1)
def searchForRange(array,target):
    start = -1
    end = -1
    
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            if mid == 0 or array[mid-1] != target:
                start = mid
                break
            else:
                right = mid -1
                
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            if mid == len(array) - 1 or array[mid + 1] != target:
                end = mid
                break
            else:
                left = mid + 1
                
    return [start,end]

print(searchForRange([0,1,4,4,4,4,21,33,45,45,61,71,73],4))

# by me, without looking, very good, very proud