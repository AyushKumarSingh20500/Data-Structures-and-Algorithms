# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# def list_to_LL(array):
#     if len(array) == 0:
#         return None
    
#     head = Node(array[0])
#     tail = head
#     for i in range(1,len(array)):
#         newNode = Node(array[i])
#         tail.next = newNode
#         tail = newNode
        
#     return head

# head = list_to_LL([1,2,3,4,5])

# def print_LL(head):
#     while head:
#         print(head.value,end="-->")
#         head = head.next
#     print("None")

# print_LL(head)

# =====================================

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# def input_for_LL(myinput):
#     array = list(map(int, myinput.split()))
    
#     head = Node(array[0])
#     tail = head
#     for i in range(1,len(array)):
#         newNode = Node(array[i])
#         tail.next = newNode
#         tail = newNode
        
#     return head

# coding_ninjas_head = input_for_LL("1 2 3 4 5")

# def print_LL(head):
#     while head:
#         print(head.value,end="-->")
#         head = head.next
#     print("None")

# print_LL(coding_ninjas_head)

# =====================================

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def list_to_LL(array):
    if len(array) == 0:
        return None
    
    head = Node(array[0])
    tail = head
    for i in range(1,len(array)):
        newNode = Node(array[i])
        tail.next = newNode
        tail = newNode
        
    return head

head = list_to_LL([1,2,3,4,5,6,7,8,9])

def print_LL(head):
    while head:
        print(head.value, end="-->")
        head = head.next
    print("None")
    
print_LL(head)

def length_LL(head):
    counter = 0
    while head:
        counter = counter + 1
        head = head.next
        
    return counter

print(length_LL(head))

def print_ith_in_LL(head,idx):
    curr = head
    for i in range(idx):
        curr = curr.next
        
    return curr.value

print(print_ith_in_LL(head,2))

def insert_at_ith_in_LL(head,idx,value):
    prev = None
    curr = head
    for i in range(idx):
        prev = curr
        curr = curr.next
        
    newNode = Node(value)
    
    if idx == 0:
        newNode.next = curr
        head = newNode
    else:
        prev.next = newNode
        newNode.next = curr
    
    return head

# inserted_head = insert_at_ith_in_LL(head,0,99) # Working fine, commedted bcoz it was interupting delete_ith_in_LL function.

# print_LL(inserted_head)

def delete_ith_in_LL(head,idx):
    prev = None
    curr = head
    for i in range(idx):
        prev = curr
        curr = curr.next
        
    if idx == 0:
        head = curr.next
    else:
        prev.next = curr.next
    
    return head

# deleted_head = delete_ith_in_LL(head,4)

# print_LL(deleted_head)

def length_LL_recursive(head):
    if head == None:
        return 0
    else:
        return 1 + length_LL_recursive(head.next)
    
print(length_LL_recursive(head))

def insert_at_ith_in_LL_recursive(head,idx,value): #by me, without looking, very good, very proud
    if idx == 0:
        newNode = Node(value)
        newNode.next = head
        head = newNode
        return head
    else:
        head.next = insert_at_ith_in_LL_recursive(head.next,idx-1,value)
        return head
        
# inserted_head_recursive = insert_at_ith_in_LL_recursive(head,9,69)

# print_LL(inserted_head_recursive)

def delete_ith_in_LL_recursive(head,idx):
    if idx == 0:
        head = head.next
        return head
    else:
        head.next = delete_ith_in_LL_recursive(head.next,idx-1)
        return head
    
deleted_head_recursive = delete_ith_in_LL_recursive(head,2)

print_LL(deleted_head_recursive)