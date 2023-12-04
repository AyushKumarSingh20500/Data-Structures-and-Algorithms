# Time: O(n*m), n = number of words in array and m = length of a single word | Space: O(c), c = number of unique character in maxCount dictionary
# Remember: c <= n * m | So total time complexity is O(n*m)+c => O(n*m)+(n*m) => O 2(n*m) => O(n*m)
def mininumCharactersForWords(array):
    result = []
    maxCount = {}
    for word in array:
        currCount = {}
        for char in word:
            if char in currCount.keys():
                currCount[char] += 1
            else:
                currCount[char] = 1
                
        for key,value in currCount.items():
            if key in maxCount.keys():
                maxCount[key] = max(maxCount[key],currCount[key])
            else:
                maxCount[key] = value
                
    for key,value in maxCount.items():
        for i in range(value):
            result.append(key)
            
    return result

print(mininumCharactersForWords(["this","that","did","deed","them!","a"]))

# by me, without looking, very good, very proud