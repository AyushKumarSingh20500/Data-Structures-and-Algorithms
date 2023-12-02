# # Time: O(n**2), n = length of array | Space: O(1)
# def twoSum(arr, target):
#     for i in range(len(arr) - 1):
#         for j in range(i+1, len(arr)):
#             if(arr[i]+arr[j] == target):
#                 return [arr[i], arr[j]]
            
#     return [-1,-1]

# print(twoSum([3,5,-4,8,11,1,-1,6], 10))

# -------------------------------------------

# # Time: O(n), n = length of array | Space: O(n), n = length of array
# def twoSum(arr, target):
#     lookup = {}
#     for num in arr:
#         if(target - num in lookup.keys()):
#             return [target - num, num]
#         else:
#             lookup[num] = True
            
#     return [-1,-1]

# print(twoSum([3,5,-4,8,11,1,-1,6], 10))

# ---------------------------------------------

# # Time: O(nlogn), sorting + iterating, Space: O(1)
# def twoSum(arr, target):
#     arr.sort()
#     left = 0
#     right = len(arr) - 1
#     while left < right:
#         if(arr[left] + arr[right] > target):
#             right = right - 1
#         elif(arr[left] + arr[right] < target):
#             left = left + 1
#         else:
#             return [arr[left], arr[right]]
        
#     return [-1,-1]

# print(twoSum([3,5,-4,8,11,1,-1,6], 10))

# Time: O(n**2), n = length of arr | Space: O(1)
# def twoSum(arr,target):
#     result = []
#     for i in range(len(arr) - 1):
#         for j in range(i+1,len(arr)):
#             if(arr[i] + arr[j] == target):
#                 result.append([arr[i],arr[j]])
                
#     return result

# print(twoSum([3,5,-4,8,11,1,-1,6], 10))

# Time: O(n), n = length of arr | Space: O(n), n = length of result
# def twoSum(arr,target):
#     lookup = {}
#     result = []
#     for num in arr:
#         if(target - num in lookup.keys()):
#             result.append([target-num, num])
#         else:
#             lookup[num] = True
            
#     return result

# print(twoSum([3,5,-4,8,11,1,-1,6], 10))

# Time: O(nlogn), sorting + iterating | Space: O(1)
def twoSum(arr,target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    result = []
    while left < right:
        if(arr[left] + arr[right] < target):
            left = left + 1
        elif(arr[left] + arr[right] > target):
            right = right - 1
        else:
            result.append([arr[left],arr[right]])
            left = left + 1
            right = right - 1
            
    return result

print(twoSum([3,5,-4,8,11,1,-1,6], 10))
