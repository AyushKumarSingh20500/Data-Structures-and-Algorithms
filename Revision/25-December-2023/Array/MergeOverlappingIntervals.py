def mergeOverlappingIntervals(array):
    array.sort(key = lambda x:x[0])
    result = [array[0]]
    for idx in range(1,len(array)):
        if array[idx][0] <= result[-1][1]:
            result[-1][1] = array[idx][1]
        else:
            result.append(array[idx])
            
    return result

print(mergeOverlappingIntervals([[1,2],[3,5],[4,7],[6,8],[9,10]]))
