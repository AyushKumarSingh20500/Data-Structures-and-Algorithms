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

def findANodeInLL(head,value):
    idx = 0
    while head:
        if head.value == value:
            return idx
        else:
            head = head.next
            idx = idx + 1
            
    return -1

print(findANodeInLL(head,3))