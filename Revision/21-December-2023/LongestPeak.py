def longestPeak(array):
    length = 0
    for idx in range(1,len(array) - 1):
        if array[idx-1] < array[idx] and array[idx+1] < array[idx]:
            start = idx
            end = idx
            
            while array[start-1] < array[start]:
                start = start - 1
                
            while array[end+1] < array[end]:
                end = end + 1
                
            currentLength = (end - start) + 1
            
            if currentLength > length:
                length = currentLength
                
    return length

print(longestPeak([1,2,3,3,4,0,10,6,5,-1,-3,2,3]))