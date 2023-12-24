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

head = list_to_LL([1,2,3,4,5])

def print_LL(head):
    while head:
        print(head.value,end="-->")
        head = head.next
    print("None")

print_LL(head)

def appendLastNToFirst(head,num):
    slow = head
    fast = head
    for i in range(num):
        fast = fast.next
        
    while fast.next != None:
        slow = slow.next
        fast = fast.next
        
    fast.next = head
    head = slow.next
    slow.next = None
    
    return head

appended_head = appendLastNToFirst(head,2)

print_LL(appended_head)