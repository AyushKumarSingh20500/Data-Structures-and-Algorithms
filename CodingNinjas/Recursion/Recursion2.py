# def replace(string,a,b,idx = 0):
#     if len(string) == idx:
#         return ""
    
#     if string[idx] == a:
#         return b + replace(string,a,b,idx+1)
#     else:
#         return string[idx] + replace(string,a,b,idx+1)
    
# print(replace("bbabb","a","z"))

# ===================================

# def removeX(string,idx = 0):
#     if len(string) == idx:
#         return ""
    
#     if string[idx] == "x":
#         return removeX(string,idx+1)
#     else:
#         return string[idx] + removeX(string,idx+1)
    
# print(removeX("xayuxshx"))

# ===================================

# def replacePI(string,idx = 0):
#     if len(string) == idx:
#         return ""
    
#     if string[idx:idx+2] == "pi":
#         return "3.14" + replacePI(string,idx+2)
#     else:
#         return string[idx] + replacePI(string,idx+1)
    
# print(replacePI("ayupish"))

# ===================================

# def replaceDuplicate(string,idx = 0):
#     if len(string) == idx:
#         return ""
    
#     if len(string) - 1 == idx:
#         return string[idx]
    
#     if string[idx] == string[idx+1]:
#         return replaceDuplicate(string,idx+1)
#     else:
#         return string[idx] + replaceDuplicate(string,idx+1)
    
# print(replaceDuplicate("xxxyyyzwwzzz"))

# ===================================

# def toweOfHanoi(n,source,helper,destination):
#     if n == 1:
#         print(f"move {n}th disk from {source} to {destination}")
#         return
        
#     toweOfHanoi(n-1,source,destination,helper)
#     print(f"move {n}th disk from {source} to {destination}")
#     toweOfHanoi(n-1,helper,source,destination)
    
# toweOfHanoi(3,"source","helper","destination")