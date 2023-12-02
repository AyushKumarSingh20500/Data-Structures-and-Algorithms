# Time: O(nlogn), sorting + iterating | Space: O(1)
# def nonConstructibleChange(arr):
#     arr.sort()
#     change = 0
#     for num in arr:
#         if(num > change + 1):
#             return change + 1
#         else:
#             change = change + num
            
#     return change + 1

# print(nonConstructibleChange([5,7,1,1,2,3,22]))

# by me, without looking


def solution(arr):
    arr.sort()
    change = 0
    for num in arr:
        if(num > change + 1):
            return change + 1
        else:
            change = change + num
            
    return change + 1

print(solution([5,7,1,1,2,3,22]))
