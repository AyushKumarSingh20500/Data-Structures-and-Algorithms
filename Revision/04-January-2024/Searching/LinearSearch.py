def linearSearch(array,target):
    for idx in range(len(array)):
        if array[idx] == target:
            return idx
        
    return -1

print(linearSearch([1,2,3,4,5],4))