def smallestDifference(array1,array2):
    array1.sort()
    array2.sort()
    idx1 = 0
    idx2 = 0
    difference = float("inf")
    value1 = 0
    value2 = 0
    while idx1 < len(array1) and idx2 < len(array2):
        if array1[idx1] < array2[idx2]:
            currentDifference = array2[idx2] - array1[idx1]
            if currentDifference < difference:
                difference = currentDifference
                value1 = array1[idx1]
                value2 = array2[idx2]
            idx1 = idx1 + 1
        elif array1[idx1] > array2[idx2]:
            currentDifference = array1[idx1] - array2[idx2]
            if currentDifference < difference:
                difference = currentDifference
                value1 = array1[idx1]
                value2 = array2[idx2]
            idx2 = idx2 + 1
        else:
            return [value1,value2]
            
    return [value1,value2]

print(smallestDifference([-1,5,10,20,28,3],[26,134,135,15,17]))

# by me, without looking, very good, very proud

# refactor it