def runLengthEncoding(string):
    result = []
    count = 1
    for i in range(1,len(string)):
        if string[i-1] == string[i] and count < 9:
            count += 1
        else:
            result.append(str(count))
            result.append(string[i-1])
            count = 1
            
    result.append(str(count))
    result.append(string[-1])
    
    return "".join(result)

print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))