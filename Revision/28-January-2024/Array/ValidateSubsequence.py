def validateSubsequence(sequence,subsequence):
    for num in sequence:
        if subsequence:
            if num == subsequence[0]:
                subsequence.pop(0)
                
    return len(subsequence) == 0

print(validateSubsequence([5,1,22,25,6,-1,8,10], [1,6,-1,10,]))