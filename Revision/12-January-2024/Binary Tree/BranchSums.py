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

def branchSums(root):
    result = []
    branchSumsHelper(root,0,result)
    return result

def branchSumsHelper(root,currentSum,result):
    if root == None:
        return 0
    
    currentSum += root.value
    if root.left == None and root.right == None:
        result.append(currentSum)
        
    branchSumsHelper(root.left,currentSum,result)
    branchSumsHelper(root.right,currentSum,result)

print(branchSums(a))