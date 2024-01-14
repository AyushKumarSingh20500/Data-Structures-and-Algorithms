def generateDocument(characters,document):
    frequency = {}
    for char in characters:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
    for char in document:
        if char not in frequency:
            return False
        else:
            if frequency[char] >= 1:
                frequency[char] -= 1
            else:
                return False
            
    return True

print(generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))
