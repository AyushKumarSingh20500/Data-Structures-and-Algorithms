def monotonicArray(array):
    direction = 0
    for idx in range(1,len(array)):
        if direction == 1:
            if array[idx] < array[idx-1]:
                return False
        elif direction == -1:
            if array[idx] > array[idx-1]:
                return False
        else:
            if array[idx-1] < array[idx]:
                direction = 1
            elif array[idx-1] > array[idx]:
                direction = -1
            else:
                continue
            
    return True

print(monotonicArray([-1,-5,-10,-1100,-1100,-1101,-1102,-9001]))
print(monotonicArray([1,1,1,1,2,3,3,3,3,4,6]))
