class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def list_to_LinkedList(array):
    if len(array) == 0:
        return None
    
    head = Node(array[0])
    tail = head
    for i in range(1,len(array)):
        newNode = Node(array[i])
        tail.next = newNode
        tail = newNode
        
    return head

head = list_to_LinkedList([1,2,3,4,5,6,7,8])

def print_LinkedList(head):
    while head:
        print(head.value,end="-->")
        head = head.next
    print("None")

print_LinkedList(head)

def middleNode(head):
    slow = head
    fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        
    return slow.value

print(middleNode(head))