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
# e.left = j
c.left = f
c.right = g

def BFS(root):
    queue = []
    queue.append(root)
    
    while len(queue) != 0:
        current = queue.pop(0)
        
        print(current.value, end=" ")
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

BFS(a)
print("")
def invertBinaryTree(root):
    if root == None:
        return
    
    invertBinaryTree(root.left)
    invertBinaryTree(root.right)
    
    temp = root.left
    root.left = root.right
    root.right = temp

invertBinaryTree(a)

BFS(a)