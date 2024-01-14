def reverseWordsInString(string):
    result = []
    idx = 0
    while idx < len(string):
        if string[idx] == " ":
            result.insert(0," ")
            idx += 1
        else:
            start = idx
            end = idx
            while idx < len(string) and string[idx] != " ":
                end += 1
                idx += 1
                
            result.insert(0,string[start:end])
            
    return "".join(result)

print(reverseWordsInString("AlgoExpert is the best!"))