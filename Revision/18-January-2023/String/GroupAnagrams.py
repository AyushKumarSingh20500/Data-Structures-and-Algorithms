def groupAnagrams(anagrams):
    lookup = {}
    for word in anagrams:
        key = [0] * 26
        for char in word:
            index = ord(char) - 97
            key[index] += 1
            
        if tuple(key) in lookup:
            lookup[tuple(key)].append(word)
        else:
            lookup[tuple(key)] = [word]
            
    return list(lookup.values())

print(groupAnagrams(["yyo","act","flop","tac","cat","oyy","olfp"]))