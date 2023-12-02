# Time: O(n), n = length of array | Space: O(1)
def monotonicArray(arr):
    direction = 0
    for i in range(1, len(arr)):
        if(direction == 1):
            if(arr[i] >= arr[i-1]):
                continue
            else:
                return False
        elif(direction == -1):
            if(arr[i] <= arr[i-1]):
                continue
            else:
                return False
        else:
            if(arr[i] > arr[i-1]):
                direction = 1
            elif(arr[i] < arr[i-1]):
                direction = -1
            else:
                continue
            
    return True

# print(monotonicArray([1,1,1,1,2,3,3,3,3,4,6]))

print(monotonicArray([-1,-5,-10,-1100,-1100,-1101,-1102,-9001]))

# by me, without looking