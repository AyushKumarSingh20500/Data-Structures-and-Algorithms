# Time: O(n), n = length of array | Space: O(n), n = length of lookup
# def firstDuplicateValue(arr):
#     lookup = {}
#     for num in arr:
#         if(num in lookup.keys()):
#             return num
#         else:
#             lookup[num] = True
            
#     return -1

# print(firstDuplicateValue([2,1,5,3,4]))

# by me, without looking

# -------------------------------------------------

# Time: O(n), n = length of array | Space: O(1)
def firstDuplicateValue(arr):
    for num in arr:
        index = abs(num) - 1
        if(arr[index] < 0):
            return abs(num)
        else:
            arr[index] = -1 * arr[index]
            
    return -1

print(firstDuplicateValue([5,1,3,2,5,3]))

# by me, without looking