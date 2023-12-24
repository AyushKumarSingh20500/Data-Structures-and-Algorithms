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

head = list_to_linked_list([1,2,3,2,1,5])

def print_LL(head):
    while head:
        print(head.value,end="-->")
        head = head.next
    print("None")

print_LL(head)

def reverse_LL(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        
    return prev

def palindromeLL(head):
    head1 = head
    tail1 = None
    slow = head
    fast = head
    while fast != None and fast.next != None:
        tail1 = slow
        slow = slow.next
        fast = fast.next.next
        
    tail1.next = None
    
    head2 = slow
    
    head2 = reverse_LL(head2)
    
    while head1 != None and head2 != None:
        if head1.value != head2.value:
            return False
        else:
            head1 = head1.next
            head2 = head2.next
            
    return True

print(palindromeLL(head))