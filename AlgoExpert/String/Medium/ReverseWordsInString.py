# Time: O(n + m), n = length of string and m = length of a word | Space: O(n+m), n = length of result and m = length of reversedResult
def reverseWordsInString(string):
    result = []
    i = 0
    while i <= len(string) - 1:
        if(string[i] == " "):
            result.append(string[i])
            i = i + 1
        elif(string[i] != " "):
            start = i
            end = i
            while end <=len(string) - 1 and string[end] != " ":
                end = end + 1
            word = string[start:end]
            result.append(word)
            i = i + (end - start)
            
    reversedResult = []
    for revIdx in range(len(result)-1,-1,-1):
        reversedResult.append(result[revIdx])
        
    return "".join(reversedResult)

print(reverseWordsInString("AlgoExpert is the best!"))

# by me, without looking, very good, very proud