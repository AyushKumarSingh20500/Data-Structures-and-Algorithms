# Time: O(n), n = length of arr | Space: O(1)
def longestPeak(arr):
    peak = -float("inf")
    for i in range(1, len(arr) - 1):
        if(arr[i] > arr[i-1] and arr[i] > arr[i+1]):
            start = i
            end = i
            while(arr[start] > arr[start - 1]):
                start = start - 1
            
            while(arr[end] > arr[end + 1]):
                end = end + 1
            
            currentPeak = (end - start) + 1
            
            if(currentPeak > peak):
                peak = currentPeak
                
    return peak

print(longestPeak([1,2,3,3,4,0,10,6,5,-1,-3,2,3]))

# by me, without looking