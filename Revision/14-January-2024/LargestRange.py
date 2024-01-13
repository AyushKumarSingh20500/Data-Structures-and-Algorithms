def largestRange(array):
    mainCount = 0
    result = [0,0]
    for num in array:
        if num - 1 in array:
            continue
        else:
            start = num
            end = num
            currCount = 0
            
            while end + 1 in array:
                end = end + 1
                currCount += 1
            
            if currCount > mainCount:
                mainCount = currCount
                result = [start,end]
                
    return result

print(largestRange([1,11,3,0,15,5,2,4,10,7,12,6]))
