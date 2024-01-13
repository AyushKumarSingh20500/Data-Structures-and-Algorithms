def longestPeak(array):
    biggestPeak = float("-inf")
    for idx in range(1,len(array)-1):
        if array[idx - 1] < array[idx] and array[idx] > array[idx + 1]:
            start = idx
            end = idx
            
            while array[start - 1] < array[start]:
                start = start - 1
                
            while array[end + 1] < array[end]:
                end = end + 1
                
            currentPeak = (end - start) + 1
            if currentPeak > biggestPeak:
                biggestPeak = currentPeak
                
    return biggestPeak

print(longestPeak([1,2,3,3,4,0,10,6,5,-1,-3,2,3]))