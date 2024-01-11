class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)
i = Node(9)
j = Node(10)

a.left = b
a.right = c
b.left = d
b.right = e
d.left = h
d.right = i
e.left = j
c.left = f
c.right = g

def branchSums(root,k):
    result = []
    branchSumsHelper(root,k,0,"",result)
    return result

def branchSumsHelper(node,k,runningSum,currentPath,result):
    if node == None:
        return
    
    runningSum += node.value
    currentPath += str(node.value) + " "
    if (node.left == None and node.right == None) and runningSum == k:
        result.append(currentPath)
        
    branchSumsHelper(node.left,k,runningSum,currentPath,result)
    branchSumsHelper(node.right,k,runningSum,currentPath,result)

print(branchSums(a,10))