# Time: O(n), n = length of array | Space: O(n), n = length of array
def sortedSquaredArray(arr):
    result = [0] * len(arr)
    small = 0
    large = len(arr) - 1
    idx = -1
    while small <= large:
        if(abs(arr[small]) > abs(arr[large])):
            # small = small + 1
            # result.insert(idx, arr[small]**2)
            result[idx] = arr[small]**2
            small = small + 1
            idx = idx - 1
        elif(abs(arr[small]) < abs(arr[large])):
            # large = large - 1
            # result.insert(idx, arr[large]**2)
            result[idx] = arr[large]**2
            large = large - 1
            idx = idx - 1
        else:
            # small = small + 1
            # large = large - 1
            # result.insert(idx, arr[large]**2)
            result[idx] = arr[large]**2
            small = small + 1
            large = large - 1
            idx = idx - 1
            
    return result

print(sortedSquaredArray([1,2,3,4,5,6,7,8,9]))

print(sortedSquaredArray([-4,-2,0,1,3]))
