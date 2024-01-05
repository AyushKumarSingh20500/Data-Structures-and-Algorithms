def permutations(array):
    result = []
    
    if len(array) == 1:
        return [[array[0]]]
    
    for i in range(len(array)):
        num = array.pop(0)
        perms = permutations(array)
        
        for perm in perms:
            perm.append(num)
            
        result.extend(perms)
        
        array.append(num)
        
    return result

print(permutations([1,2,3]))