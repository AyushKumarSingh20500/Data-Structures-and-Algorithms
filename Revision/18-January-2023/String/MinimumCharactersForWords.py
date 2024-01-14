def minimumCharactersForWords(array):
    result = []
    maxCount = {}
    for word in array:
        currentCount = {}
        for char in word:
            if char in currentCount:
                currentCount[char] += 1
            else:
                currentCount[char] = 1
                
        for key,value in currentCount.items():
            if key in maxCount:
                maxCount[key] = max(maxCount[key],currentCount[key])
            else:
                maxCount[key] = value
                
    for key,value in maxCount.items():
        for i in range(value):
            result.append(key)
            
    return result

print(minimumCharactersForWords(["this","that","did","deed","them!","a"]))