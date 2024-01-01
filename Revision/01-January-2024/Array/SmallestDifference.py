def smallestDifference(array1,array2):
    array1.sort()
    array2.sort()
    
    array1Idx = 0
    array2Idx = 0
    
    minimumDifference = float("inf")
    result = [0,0]
    while array1Idx < len(array1) and array2Idx < len(array2):
        if array1[array1Idx] < array2[array2Idx]:
            currenctDifference = array2[array2Idx] - array1[array1Idx]
            if currenctDifference < minimumDifference:
                minimumDifference = currenctDifference
                result[0] = array1[array1Idx]
                result[1] = array2[array2Idx]
            array1Idx = array1Idx + 1
        elif array1[array1Idx] > array2[array2Idx]:
            currenctDifference = array1[array1Idx] - array2[array2Idx]
            if currenctDifference < minimumDifference:
                minimumDifference = currenctDifference
                result[0] = array1[array1Idx]
                result[1] = array2[array2Idx]
            array2Idx = array2Idx + 1
        else:
            return [array1[array1Idx],array2[array2Idx]]
        
        
            
    return result

print(smallestDifference([-1,5,10,20,28,3],[26,134,135,15,17]))
print(smallestDifference([-1,5,10,20,28,3],[26,134,135,15,17]))
