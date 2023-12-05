# Time: O(n), n = length of array | Space: O(1)
def linearSearch(array,target):
    for num in array:
        if num == target:
            return True
        
    return False

print(linearSearch([1,2,3,4,5],4))