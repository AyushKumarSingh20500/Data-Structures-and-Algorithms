def spiralTraverse(matrix):
    result = []
    startRow = 0
    endRow = len(matrix) - 1
    startCol = 0
    endCol = len(matrix[0]) - 1
    
    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol,endCol):
            result.append(matrix[startRow][col])
            
        for row in range(startRow,endRow):
            result.append(matrix[row][endCol])
            
        for col in reversed(range(startCol+1,endCol+1)):
            result.append(matrix[endRow][col])
            
        for row in reversed(range(startRow+1,endRow+1)):
            result.append(matrix[row][startCol])
            
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