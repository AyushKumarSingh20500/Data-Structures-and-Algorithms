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

def height(root):
    if root == None:
        return 0
    
    left = height(root.left)
    right = height(root.right)
    
    return 1 + max(left,right)

def binaryTreeDiameter(root):
    if root == None:
        return 0
    
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    
    rootDiameter = leftHeight + rightHeight
    
    leftDiameter = binaryTreeDiameter(root.left)
    rightDiameter = binaryTreeDiameter(root.right)
    
    return max(rootDiameter, leftDiameter, rightDiameter)

print(binaryTreeDiameter(a))