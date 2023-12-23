class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)

# # print(a.value)
# # print(a.next)

# a.next = b
# b.next = c
# c.next = d

# print(a.value)
# print(a.next.value)
# print(a.next.next.value)

# ===============================================

# def list_to_linked_list(array):
#     if len(array) == 0:
#         return None
    
#     head = Node(array[0])
#     curr = head
#     for i in range(1,len(array)):
#         new = Node(array[i])
#         curr.next = new
#         curr = new
        
#     return head

# head = list_to_linked_list([1,2,3,4,5])

# def print_linked_list(head):
#     while head:
#         print(head.value,end="-->")
#         head = head.next
#     print("None")
    
# print_linked_list(head)


# ===============================================

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def list_to_linked_list(array):
    if len(array) == 0:
        return None
    
    head = Node(array[0])
    tail = head
    for i in range(1,len(array)):
        newNode = Node(array[i])
        tail.next = newNode
        tail = newNode
        
    return head

head = list_to_linked_list([1,2,3,4,5,6])

def print_linked_list(head):
    while head:
        print(head.value,end="-->")
        head = head.next
    print("None")
    
print_linked_list(head)

def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        
    return prev

reversed_head = reverse_linked_list(head)

print_linked_list(reversed_head)

# =====================================

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e
# e.next = b

def print_linked_list(head):
    while head:
        print(head.value,end="-->")
        head = head.next
    print("None")
    
# print_linked_list(a)

def cycle_check(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
        
    return False

print(cycle_check(a))

def nth_to_the_last(head,node):
    slow = head
    fast = head
    for i in range(node-1):
        if fast.next == None:
            print("going out of bound")
            return
        else:
            fast = fast.next
        
    while fast.next != None:
        slow = slow.next
        fast = fast.next
        
    return slow.value

print(nth_to_the_last(a,2))