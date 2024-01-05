def powerSet(array):
    result = [[]]
    for ele in array:
        for idx in range(len(result)):
            result.append(result[idx] + [ele])
            
    return result

print(powerSet([1,2,3]))