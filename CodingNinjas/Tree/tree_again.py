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

def preorder(root):
    if root == None:
        return 
    
    print(root.value, end=" ")
    preorder(root.left)
    preorder(root.right)

preorder(a)

print("")

def inorder(root):
    if root == None:
        return
    
    inorder(root.left)
    print(root.value, end=" ")
    inorder(root.right)

inorder(a)

print("")

def postorder(root):
    if root == None:
        return 
    
    postorder(root.left)
    postorder(root.right)
    print(root.value, end=" ")

postorder(a)

print("")

# def preorderIndetail(root):
#     if root == None:
#         return 
    
#     print(root.value, end=": ")
#     if root.left != None:
#         print(f"L: {root.left.value}", end=" ")
#     if root.right != None:
#         print(f"R: {root.right.value}",end="")
#     print("")
#     preorderIndetail(root.left)
#     preorderIndetail(root.right)

# preorderIndetail(a)

# def binaryTreeBasedOnInput():
#     value = int(input())
#     if value == -1:
#         return None
    
#     root = Node(value)
#     left = binaryTreeBasedOnInput()
#     right = binaryTreeBasedOnInput()
    
#     root.left = left
#     root.right = right
    
#     return root

# root = binaryTreeBasedOnInput()

# preorder(root)

def BFS(root):
    queue = []
    queue.append(root)
    while len(queue) != 0:
        current = queue.pop(0)
        print(current.value, end=" ")
        
        if current.left != None:
            queue.append(current.left)
            
        if current.right != None:
            queue.append(current.right)

BFS(a)

print("")

def numberOfNodesInBT(root):
    if root == None:
        return 0
    
    left = numberOfNodesInBT(root.left)
    right = numberOfNodesInBT(root.right)
    
    return 1 + left + right

print(numberOfNodesInBT(a))

def sumOfNodes(root):
    if root == None:
        return 0
    
    left = sumOfNodes(root.left)
    right = sumOfNodes(root.right)
    
    return root.value + left + right

print(sumOfNodes(a))

def nodeWithLargestValue(root):
    if root == None:
        return -1
    
    left = nodeWithLargestValue(root.left)
    right = nodeWithLargestValue(root.right)
    
    return max(root.value, left, right)

print(nodeWithLargestValue(a))

def nodeGreaterThanX(root,X):
    if root == None:
        return 0
    
    count = 0
    if root.value > X:
        count += 1
    
    count += nodeGreaterThanX(root.left,X)
    count += nodeGreaterThanX(root.right,X)
    
    return count

print(nodeGreaterThanX(a,5))