def smallestDifference(array1,array2):
    array1.sort()
    array2.sort()
    idx1 = 0
    idx2 = 0
    result = [0,0]
    minimumDifference = float("inf")
    while idx1 < len(array1) and idx2 < len(array2):
        firstNumber = array1[idx1]
        secondNumber = array2[idx2]
        if firstNumber > secondNumber:
            currentDifference = firstNumber - secondNumber
            idx2 = idx2 + 1
        elif firstNumber < secondNumber:
            currentDifference = secondNumber - firstNumber
            idx1 = idx1 + 1
        else:
            return [firstNumber,secondNumber]
            
        if currentDifference < minimumDifference:
            minimumDifference = currentDifference
            result = [firstNumber,secondNumber]
            
    return result

print(smallestDifference([-1,5,10,20,28,3],[26,134,135,15,17]))
