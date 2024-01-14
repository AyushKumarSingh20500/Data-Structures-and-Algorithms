def longestPalindromicSubstring(string):
    longestPalindrome = ""
    longestLength = 0
    for i in range(len(string)):
        # odd palindrome
        start = i
        end = i
        while start >= 0 and end <= len(string) - 1 and string[start] == string[end]:
            currentLength = (end - start) + 1
            if currentLength > longestLength:
                longestLength = currentLength
                longestPalindrome = string[start:end+1]
            start -= 1
            end += 1
            
        # even palindrome
        start = i
        end = i+1
        while start >= 0 and end <= len(string) - 1 and string[start] == string[end]:
            currentLength = (end - start) + 1
            if currentLength > longestLength:
                longestLength = currentLength
                longestPalindrome = string[start:end+1]
            start -= 1
            end += 1
            
            
    return longestPalindrome

print(longestPalindromicSubstring("abaxyzzyxf"))