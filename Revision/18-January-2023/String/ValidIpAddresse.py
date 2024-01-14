def validIpAddress(string):
    IPAddresses = []
    
    for idx in range(1,min(len(string),4)):
        currentIP = ["","","",""]
        
        currentIP[0] = string[0:idx]
        if not isValid(currentIP[0]):
            continue
        
        for jdx in range(idx+1,min(len(string),idx+4)):
            currentIP[1] = string[idx:jdx]
            if not isValid(currentIP[1]):
                continue
            
            for kdx in range(jdx+1,min(len(string),jdx+4)):
                currentIP[2] = string[jdx:kdx]
                currentIP[3] = string[kdx:]
                
                if isValid(currentIP[2]) and isValid(currentIP[3]):
                    IPAddresses.append(".".join(currentIP))
                    
    return IPAddresses

def isValid(string):
    intOfString = int(string)
    
    if intOfString > 255:
        return False
    else:
        return len(string) == len(str(intOfString))


print(validIpAddress("1921680"))