def findThreeLargestNumbers(array):
    result = [0] * 3
    for num in array:
        for largeNum in reversed(range(3)):
            if result[largeNum] == 0:
                result[largeNum] = num
                break
            elif result[largeNum] > num:
                continue
            elif result[largeNum] < num:
                result[largeNum - 1], result[largeNum] = result[largeNum], num
                break
                
    return result

print(findThreeLargestNumbers([141,1,17,-7,-17,-27,19,541,8,7,7]))

# wrong code