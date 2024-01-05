def staircaseTraversal(height,steps):
    if height == 0:
        return 1
    elif height == 1:
        return 1
    else:
        result = 0
        for step in range(1,min(height,steps) + 1):
            result = result + staircaseTraversal(height-step,steps)
            
        return result

print(staircaseTraversal(4,3))