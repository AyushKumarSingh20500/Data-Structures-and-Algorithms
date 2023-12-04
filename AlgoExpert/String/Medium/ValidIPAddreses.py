# Time: O(1) | Space: O(1)
def validIPAdresses(string):
    IPAdresses = []
    for i in range(1,min(len(string),4)):
        currentIPAddress = ["","","",""]
        
        currentIPAddress[0] = string[:i]
        
        if not isValid(currentIPAddress[0]):
            continue
        
        for j in range(i+1,min(len(string),i+4)):
            currentIPAddress[1] = string[i:j]
            
            if not isValid(currentIPAddress[1]):
                continue
            
            for k in range(j+1,min(len(string),j+4)):
                currentIPAddress[2] = string[j:k]
                currentIPAddress[3] = string[k:]
                
                if isValid(currentIPAddress[2]) and isValid(currentIPAddress[3]):
                    IPAdresses.append(".".join(currentIPAddress))
                    
    return IPAdresses

def isValid(string):
    stringAsInt = int(string)
    if stringAsInt > 255:
        return False
    
    return len(string) == len(str(stringAsInt))

print(validIPAdresses("1921680"))