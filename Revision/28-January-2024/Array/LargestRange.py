def largestRange(array):
    start = 0
    end = 0
    count = 0
    for num in array:
        if num - 1 in array:
            continue
        else:
            currStart = num
            currEnd = num
            currCount = 0
            
            while currEnd + 1 in array:
                currEnd += 1
                currCount += 1
                
            if currCount > count:
                count = currCount
                start = currStart
                end = currEnd
                
    return [start,end]

print(largestRange([1,11,3,0,15,5,2,4,10,7,12,6]))