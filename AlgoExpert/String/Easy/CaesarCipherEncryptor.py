# Time: O(n), n = length of string | Space: O(n), n = length of result
def caesaeCipherEncryptor(string,key):
    result = ""
    key = key % 26
    for char in string:
        asciiIdx = ord(char)
        asciiIdx = asciiIdx + key
        
        if asciiIdx > 122:
            reminder = asciiIdx % 122
            asciiIdx = 96 + reminder
            result += chr(asciiIdx)
        else:
            result += chr(asciiIdx)
            
    return result

print(caesaeCipherEncryptor("xyz",54))

# by me, without looking