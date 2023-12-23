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

head = list_to_LL([1,1,2,3,3,3,3,4,4])

def print_LL(head):
    while head:
        print(head.value,end="-->")
        head = head.next
    print("None")
    
print_LL(head)

def eleminate_duplicates_from_LL(head):
    slow = head
    fast = head
    while fast != None:
        if slow.value == fast.value:
            fast = fast.next
        else:
            slow.next = fast
            slow = fast
            fast = fast.next
            
    slow.next = fast
    
    return head

eleminated_head = eleminate_duplicates_from_LL(head)

print_LL(eleminated_head)

# by me, without looking, very good, very proud
# not even saw theoratical solution