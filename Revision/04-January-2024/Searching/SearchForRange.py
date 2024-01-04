def searchForRange(array,target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] > target:
            right = mid - 1
        elif array[mid] < target:
            left = mid + 1
        else:
            start = mid
            end = mid
            while start >= 0 and array[start-1] == target:
                start = start - 1
                
            while end <= len(array)-1 and array[end+1] == target:
                end = end + 1
                
            return [start,end]
        
    return [-1,-1]

print(searchForRange([0,1,21,33,45,45,45,45,45,45,61,71,73],33))

# best solution I came up with