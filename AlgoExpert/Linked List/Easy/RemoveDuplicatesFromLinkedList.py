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

head = list_to_LinkedList([1,1,3,4,4,4,5,6,6])

def print_LinkedList(head):
    while head:
        print(head.value,end="-->")
        head = head.next
    print("None")

print_LinkedList(head)

def removeDuplicatesFromLinkedList(head):
    slow = head
    fast = head.next
    while fast != None:
        if slow.value == fast.value:
            fast = fast.next
        else:
            slow.next = fast
            slow = fast
            fast = fast.next
            
    slow.next = fast
    
    return head

removeDuplicatesFromLinkedListHead = removeDuplicatesFromLinkedList(head)

print_LinkedList(removeDuplicatesFromLinkedListHead)