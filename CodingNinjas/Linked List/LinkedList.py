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

head = list_to_LL([1,2,3,4,5,6,7,8])
head1 = list_to_LL([1,3,5,7,9])
head2 = list_to_LL([0,2,4,6,8])

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
    
# deleted_head_recursive = delete_ith_in_LL_recursive(head,2)

# print_LL(deleted_head_recursive)

def reverse_LL_recursive(head):
    if head == None:
        return None,None
    
    if head.next == None:
        return head,head
    else:
        smallHead, smallTail = reverse_LL_recursive(head.next)
        smallTail.next = head
        head.next = None
        return smallHead,head
    
# head,tail = reverse_LL_recursive(head)

# print_LL(head)

# print_LL(head1)
# print_LL(head2)

def merge_two_sorted_LL(head1,head2):
    curr1 = head1
    curr2 = head2
    while curr1 != None and curr2 != None:
        if curr2.value < curr1.value:
            temp = curr2.next
            curr2.next = curr1
            curr2 = temp
        else:
            temp = curr1.next
            curr1.next = curr2
            curr1 = temp
            
    if head2.value < head1.value:
        return head2
    else:
        return head1

# merged_head = merge_two_sorted_LL(head1,head2)

# print_LL(merged_head)

# by me, without looking, very good, very proud
# not even saw theoratical solution

def even_after_odd_LL(head):
    evenHead = None
    evenTail = None
    oddHead = None
    oddTail = None
    while head:
        if head.value % 2 == 0:
            if evenHead == None:
                evenHead = head
                evenTail = head
            else:
                evenTail.next = head
                evenTail = head
        else:
            if oddHead == None:
                oddHead = head
                oddTail = head
            else:
                oddTail.next = head
                oddTail = head
                
        head = head.next
        
    evenTail.next = head
    oddTail.next = evenHead
    
    return oddHead

# even_after_odd_head = even_after_odd_LL(head)

# print_LL(even_after_odd_head)

# by me, without looking, very good, very proud
# not even saw theoratical solution

def delete_every_N_Nodes(head,m,n):
    curr = head
    slow = head
    fast = head
    while curr:
        for i in range(m-1):
            if curr:
                slow = slow.next
                fast = fast.next
                curr = curr.next
                
        for i in range(n+1):
            if curr:
                fast = fast.next
                curr = curr.next
            
        if slow == None:
            return head
        else:
            slow.next = fast
            slow = fast
        
    return head

# print_LL(head)

# delete_every_N_Nodes_Head = delete_every_N_Nodes(head,2,3)

# print_LL(delete_every_N_Nodes_Head)

# by me, without looking, very good, very proud
# not even saw theoratical solution

def swap_two_node_LL(head,i,j):
    prev1 = Node(None)
    curr1 = head
    for i in range(i):
        prev1 = curr1
        curr1 = curr1.next
        
    temp1 = curr1.next
    
    prev2 = Node(None)
    curr2 = head
    for i in range(j):
        prev2 = curr2
        curr2 = curr2.next
        
    temp2 = curr2.next
    
    prev1.next = curr2
    curr2.next = temp1
    prev2.next = curr1
    curr1.next = temp2
    
    return curr2

# swapped_head = swap_two_node_LL(head,0,14)

# print_LL(swapped_head)

# by me, without looking, very good, very proud
# not even saw theoratical solution

def k_reverse_LL(head,k):
    prev = None
    curr = head
    tail = head
    counter = 0
    if counter == 4 or curr == None:
        tail.next = k_reverse_LL(curr,k)
        return prev
    else:
        while curr and counter < 4:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            counter = counter + 1
            # firstHead = prev
        return prev
    
# k_reversed_head = k_reverse_LL(head,4)

# print_LL(k_reversed_head)

def k_reverse_LL(head, k):
    prev = None
    curr = head
    tail = head
    counter = 0

    # Count the number of nodes in the current segment
    temp = head
    while temp and counter < k:
        temp = temp.next
        counter += 1

    if counter == k:
        while curr and counter > 0:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            counter -= 1

        if tail:
            tail.next = k_reverse_LL(curr, k)

        return prev
    else:
        return head
    
    
k_reversed_head = k_reverse_LL(head,3)

print_LL(k_reversed_head)