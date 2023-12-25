class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node(0)
b = Node(1)
c = Node(2)
d = Node(3)
e = Node(4)
f = Node(5)
g = Node(6)
h = Node(7)
i = Node(8)
j = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h
h.next = i
i.next = j
j.next = e

def findLoop(head):
    slow = head.next
    fast = head.next.next
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
        
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
        
    return fast.value


print(findLoop(a))