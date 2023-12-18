def powerset(array):
    subsets = [[]]
    for element in array:
        for idx in range(len(subsets)):
            subsets.append(subsets[idx] + [element])
            
    return subsets

print(powerset([1,2,3]))