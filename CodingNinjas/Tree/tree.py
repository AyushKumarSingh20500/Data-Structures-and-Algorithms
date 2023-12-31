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

def printTreePreorder(root):
    if root == None:
        return 
    
    print(root.value, end=" ")
    printTreePreorder(root.left)
    printTreePreorder(root.right)

printTreePreorder(a)

print("")

def printTreeInorder(root):
    if root == None:
        return
    
    printTreeInorder(root.left)
    print(root.value, end=" ")
    printTreeInorder(root.right)

# printTreeInorder(a)

print("")

def printTreePostoder(root):
    if root == None:
        return 
    
    printTreePostoder(root.left)
    printTreePostoder(root.right)
    print(root.value, end=" ")

# printTreePostoder(a)


def numberOfNodes(root):
    if root == None:
        return 0
    
    left = numberOfNodes(root.left)
    right = numberOfNodes(root.right)
    
    return 1 + left + right

print(numberOfNodes(a))

def sumOfNodes(root):
    if root == None:
        return 0
    
    left = sumOfNodes(root.left)
    right = sumOfNodes(root.right)
    
    return root.value + left + right

print(sumOfNodes(a))

def nodeWithLargestData(root):
    if root == None:
        return 0
    
    left = nodeWithLargestData(root.left)
    right = nodeWithLargestData(root.right)
    largest = max(left, right, root.value)
    return largest

print(nodeWithLargestData(a))

def heightOfTree(root):
    if root == None:
        return 0
    
    left = heightOfTree(root.left)
    right = heightOfTree(root.right)
    
    return 1 + max(left,right)

print(heightOfTree(a))








