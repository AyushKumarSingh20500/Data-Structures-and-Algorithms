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

head = list_to_LL([9,2,3,3,2,9])

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

def palindrome_LL(head):
    head1 = head
    prev = None
    slow = head
    fast = head
    while fast != None and fast.next != None:
        prev = slow
        slow = slow.next
        fast = fast.next.next
        
    head2 = slow
    prev.next = None
    
    reversed_head = reverse_LL(head2)
    
    while head1 != None and reversed_head != None:
        if head1.value != reversed_head.value:
            return False
        else:
            head1 = head1.next
            reversed_head = reversed_head.next
            
    return True

print(palindrome_LL(head))

# by me, without looking, very good, very proud
# not even saw theoratical solution