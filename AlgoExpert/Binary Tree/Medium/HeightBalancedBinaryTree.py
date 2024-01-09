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

a.left = b
a.right = c
b.left = d
d.left = f
c.right = e

def height(root):
    if root == None:
        return 0
    
    left = height(root.left)
    right = height(root.right)
    
    return 1 + max(left , right)

def heightBalancedBinaryTree(root):
    if root == None:
        return True
    
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    
    if abs(leftHeight - rightHeight) > 1:
        return False
    
    left = heightBalancedBinaryTree(root.left)
    right = heightBalancedBinaryTree(root.right)
    
    if left and right:
        return True
    else:
        return False

print(heightBalancedBinaryTree(a))