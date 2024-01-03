def longestPalindromicSubstring(string):
    longestPalindrome = ""
    longestLength = 0
    for idx in range(len(string)):
        # odd length palindrome
        start = idx
        end = idx
        while start >= 0 and end <= len(string) - 1:
            if string[start] == string[end]:
                currentLength = (end - start) + 1
                if currentLength > longestLength:
                    longestLength = currentLength
                    longestPalindrome = string[start:end+1]
                start -= 1
                end += 1
            else:
                break
                
        # even length palindrome
        start = idx
        end = idx + 1
        while start >= 0 and end <= len(string) - 1:
            if string[start] == string[end]:
                currentLength = (end - start) + 1
                if currentLength > longestLength:
                    longestLength = currentLength
                    longestPalindrome = string[start:end+1]
                start -= 1
                end += 1
            else:
                break
            
    return longestPalindrome

print(longestPalindromicSubstring("abaxyzzyxf"))