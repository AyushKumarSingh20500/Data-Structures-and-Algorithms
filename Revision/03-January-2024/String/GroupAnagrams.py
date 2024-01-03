def groupAnagram(array):
    lookup = {}
    for word in array:
        key = [0] * 26
        for char in word:
            index = ord(char) - 97
            key[index] = key[index] + 1
            
        if tuple(key) in lookup:
            lookup[tuple(key)].append(word)
        else:
            lookup[tuple(key)] = [word]
            
    return lookup

print(groupAnagram(["yyo","act","flop","tac","cat","oyy","olfp"]))