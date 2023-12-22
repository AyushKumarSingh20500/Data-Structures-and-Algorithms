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

def list_to_linked_list(array):
    if len(array) == 0:
        return None
    
    head = Node(array[0])
    curr = head
    for i in range(1,len(array)):
        new = Node(array[i])
        curr.next = new
        curr = new
        
    return head

head = list_to_linked_list([1,2,3,4,5])

def print_linked_list(head):
    while head:
        print(head.value,end="-->")
        head = head.next
    print("None")
    
print_linked_list(head)

