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

def findSuccessor(root,node):
    inorderTraversel = []
    findSuccessorHelper(root,inorderTraversel)
    
    for idx in range(len(inorderTraversel)):
        if idx == len(inorderTraversel) - 1:
            return None
        elif inorderTraversel[idx] == node:
            return inorderTraversel[idx+1]

def findSuccessorHelper(node,result):
    if node == None:
        return
    
    findSuccessorHelper(node.left,result)
    result.append(node.value)
    findSuccessorHelper(node.right,result)

print(findSuccessor(a,7))