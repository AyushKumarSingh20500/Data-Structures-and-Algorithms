def spiralTraverse(array):
    startRow = 0
    endRow = len(array) - 1
    startCol = 0
    endCol = len(array[0]) - 1
    result = []
    while startRow <= endRow and startCol <= endCol:
        for idx in range(startCol,endCol):
            result.append(array[startRow][idx])
            
        for idx in range(startRow,endRow+1):
            result.append(array[idx][endCol])
            
        for idx in reversed(range(startCol,endCol)):
            result.append(array[endRow][idx])
            
        for idx in reversed(range(startRow+1,endRow)):
            result.append(array[idx][startCol])
            
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
        
    return result

matrix = [[1,2,3,4],
          [12,13,14,5],
          [11,16,15,6],
          [10,9,8,7]]

print(spiralTraverse(matrix))