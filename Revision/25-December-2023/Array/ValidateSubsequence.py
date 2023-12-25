def validateSubsequence(sequence, subsequence):
    for num in sequence:
        if subsequence:
            if num == subsequence[0]:
                subsequence.pop(0)
                
    return len(subsequence) == 0

print(validateSubsequence([1,4,2,6,8,3,2],[1,2,3,4]))