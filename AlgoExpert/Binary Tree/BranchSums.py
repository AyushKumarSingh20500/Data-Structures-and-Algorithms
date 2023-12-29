class Node:
    def __init__(self,value):
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

def branchSum(root):
    result = []
    branchSumHelper(root,0,result)
    return result

def branchSumHelper(node,runningSum,result):
    if node == None:
        return
    
    newRunningSum = runningSum + node.value
    if node.left == None and node.right == None:
        result.append(newRunningSum)
        return
        
    branchSumHelper(node.left,newRunningSum,result)
    branchSumHelper(node.right,newRunningSum,result)

print(branchSum(a))