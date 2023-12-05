# Time: O(logn) | Space: O(1)
def binarySearch(array,target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            return True
        
    return False

print(binarySearch([0,1,21,33,45,45,61.71,72,73],33))

# by me, without looking