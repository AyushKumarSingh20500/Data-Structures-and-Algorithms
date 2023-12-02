# Time: O(nlogn), sorting + iterating | Space: O(n), n = length of result array
def mergeOverlappingIntervals(arr):
    sortedArr = sorted(arr, key=lambda i: i[0])
    result = [sortedArr[0]]
    current = 0
    for i in range(1, len(arr)):
        if(sortedArr[i][0] <= result[current][1]):
            result[current][1] = max(sortedArr[i][1], sortedArr[i-1][1])
        else:
            result.append(sortedArr[i])
            current = current + 1
    
    return result

print(mergeOverlappingIntervals([[3,4],[12,14],[10,15],[4,8],[1,2],[4,6]]))

# by me, without looking