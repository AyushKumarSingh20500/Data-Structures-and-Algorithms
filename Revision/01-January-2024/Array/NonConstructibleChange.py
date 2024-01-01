def nonConstructibleChange(array):
    array.sort()
    change = 0
    for num in array:
        if num > change + 1:
            return change + 1
        else:
            change = change + num
            
    return change + 1

print(nonConstructibleChange([5,7,1,1,2,3,22]))
