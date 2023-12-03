# Time: O(n), n = length of string | Space: O(n), n = length of result
def runLengthEncoding(string):
    result = []
    length = 1
    for i in range(1,len(string)):
        if(string[i] == string[i-1] and length != 9):
            length += 1
        else:
            result.append(str(length))
            result.append(string[i-1])
            length = 1
    
    result.append(str(length))
    result.append(string[len(string) - 1])
            
            
    return "".join(result)

print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))

# by me, without looking