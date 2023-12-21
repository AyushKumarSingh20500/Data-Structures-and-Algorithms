# Time: O(n), where n = length of array | Space: O(n), where n = length of array
def firstDuplicateValue(array):
    lookup = {}
    for num in array:
        if num in lookup:
            return num
        else:
            lookup[num] = 1
            
    return -1

print(firstDuplicateValue([2,1,5,2,3,3,2,4]))

# ===============================================

# Revise

# =========== After Revision ====================

def firstDuplicateValue(array):
    for num in array:
        index = abs(num) - 1
        if array[index] < 0:
            return abs(num)
        else:
            array[index] = array[index] * -1
            
    return -1

print(firstDuplicateValue([1,2,3,4,3,1,2]))

# by me, without looking, very good, very proud