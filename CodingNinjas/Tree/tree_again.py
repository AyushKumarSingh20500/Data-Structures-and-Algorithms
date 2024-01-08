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

def heightOfTree(root):
    if root == None:
        return 0
    
    left = heightOfTree(root.left)
    right = heightOfTree(root.right)
    
    return 1 + max(left,right)

print(heightOfTree(a))

def numberOfLeafInBT(root):
    if root == None:
        return 0
    
    count = 0
    if root.left == None and root.right == None:
        count += 1
    
    count += numberOfLeafInBT(root.left)
    count += numberOfLeafInBT(root.right)
    
    return count

print(numberOfLeafInBT(a))

def printNodesatDepthK(root,k):
    if root == None:
        return
    
    if k == 0:
        print(root.value, end=" ")
        
    printNodesatDepthK(root.left,k-1)
    printNodesatDepthK(root.right,k-1)

printNodesatDepthK(a,2)

print("")

# def replaceNodewithDepth(root,k = 0):
#     if root == None:
#         return
    
#     root.value = k
    
#     replaceNodewithDepth(root.left, k+1)
#     replaceNodewithDepth(root.right,k+1)
    
#     return root

# replacedRoot = replaceNodewithDepth(a)

# BFS(replacedRoot)

# print("")

# a = Node(1)
# a.left = Node(2)
# a.right = Node(3)
# a.left.left = Node(4)
# a.left.right = Node(5)

def isNodePresent(root,x): #by me, without looking very good, very proud
    if root == None:
        return False
    
    if root.value == x:
        return True
    
    left = isNodePresent(root.left,x)
    right = isNodePresent(root.right,x)
    
    return left or right

print(isNodePresent(a,10))

def nodesWithoutSibling(root):
    if root == None:
        return
    
    if (root.left != None and root.right == None) or (root.left == None and root.right != None):
        if root.left == None:
            print(root.right.value)
        elif root.right == None:
            print(root.left.value)
            
    nodesWithoutSibling(root.left)
    nodesWithoutSibling(root.right)

nodesWithoutSibling(a)



def removeLeafNodes(root):
    if root == None:
        return None
    
    if root.left == None and root.right == None:
        return None
        
    root.left = removeLeafNodes(root.left)
    root.right = removeLeafNodes(root.right)
    
    return root

# removeLeafNodesRoot = removeLeafNodes(a)

# preorder(removeLeafNodesRoot)
BFS(a)

print("Break")

def mirrorBT(root): # by me, without looking, very good very proud
    if root == None:
        return
    
    mirrorBT(root.left)
    mirrorBT(root.right)
    
    temp = root.left
    root.left = root.right
    root.right = temp

# mirrorBT(a)

# BFS(a)

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

def isBalanced(root):
    if root == None:
        return True
    
    left = heightOfTree(root.left)
    right = heightOfTree(root.right)
    
    if abs(left - right) > 1:
        return False
    
    leftBt = isBalanced(root.left)
    rightBT = isBalanced(root.right)
    
    if leftBt and rightBT:
        return True
    else:
        return False

print(isBalanced(a))