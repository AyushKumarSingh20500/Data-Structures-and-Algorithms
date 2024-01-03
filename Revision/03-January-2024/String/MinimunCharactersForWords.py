def minimumCharacterForWords(array):
    result = []
    maxFrequency = {}
    for word in array:
        currentFrequency = {}
        for char in word:
            if char in currentFrequency:
                currentFrequency[char] += 1
            else:
                currentFrequency[char] = 1
                
        for key,value in currentFrequency.items():
            if key in maxFrequency:
                maxFrequency[key] = max(maxFrequency[key],currentFrequency[key])
            else:
                maxFrequency[key] = value
                
    for key,value in maxFrequency.items():
        for i in range(value):
            result.append(key)
            
    return result

print(minimumCharacterForWords(["this","that","did","deed","them!","a"]))