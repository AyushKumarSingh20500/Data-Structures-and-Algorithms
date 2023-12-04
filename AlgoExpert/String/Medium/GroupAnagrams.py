# Time: O(n*m), n = number of words in anagram list and m = length of each word | Space: O(n), n = numbers of anagrams
def groupAnagrams(anagrams):
    lookup = {}
    for word in anagrams:
        key = [0] * 26
        for char in word:
            idx = ord(char) - 97
            key[idx] = 1
            
        if tuple(key) in lookup.keys():
            lookup[tuple(key)].append(word)
        else:
            lookup[tuple(key)] = [word]
            
    return list(lookup.values())

print(groupAnagrams(["yo","act","flop","tac","cat","oy","olfp","blog"]))

# -------------------------------------

# Time: O(w * nlogn), iterating + sorting, w = length of anagrams | Space: O(n), n = number of anagrams
def groupAnagrams(anagrams):
    lookup = {}
    for word in anagrams:
        if(tuple(sorted(word)) in lookup.keys()):
            lookup[tuple(sorted(word))].append(word)
        else:
            lookup[tuple(sorted(word))] = [word]
        
    return list(lookup.values())

print(groupAnagrams(["yo","act","flop","tac","cat","oy","olfp","blog"]))

# by me, without looking