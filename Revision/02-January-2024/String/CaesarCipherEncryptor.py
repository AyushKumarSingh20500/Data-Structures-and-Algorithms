def caesaeCipherEncryptor(string,key):
    result = ""
    key = key % 26
    for char in string:
        asciiIdx = ord(char)
        asciiIdx = asciiIdx + key
        
        if asciiIdx <= 122:
            result = result + chr(asciiIdx)
        else:
            reminder = asciiIdx % 122
            asciiIdx = 96 + reminder
            result = result + chr(asciiIdx)
            
    return result

print(caesaeCipherEncryptor("abc",1))