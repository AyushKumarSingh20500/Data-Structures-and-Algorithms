def runLengthEncoding(string):
    result = []
    count = 1
    for idx in range(1,len(string)):
        if string[idx-1] == string[idx]:
            count += 1
        else:
            result.append(str(count))
            result.append(string[idx-1])
            count = 1
            
        if count == 10:
            result.append(str(9))
            result.append(string[idx-1])
            count = 1
            
    result.append(str(count))
    result.append(string[idx])
    
    return "".join(result)

print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDDE"))