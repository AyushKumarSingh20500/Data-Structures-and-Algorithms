def caesarCipherEncryptor(string,k):
    result = ""
    k = k % 26
    for char in string:
        asciiValue = ord(char) + k
        if asciiValue <= 122:
            result = result + chr(asciiValue)
        else:
            asciiValue = 96 + (asciiValue % 122)
            result = result + chr(asciiValue)
            
    return result

print(caesarCipherEncryptor("xyz",2))