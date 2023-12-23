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

def print_LL(head):
    while head:
        print(head.value,end="-->")
        head = head.next
    print("None")
    
print_LL(head)

def find_a_node_in_LL(head,value):
    idx = 0
    while head:
        if head.value == value:
            return idx
        head = head.next
        idx = idx + 1
        
    return -1

print(find_a_node_in_LL(head,4))

# by me, without looking, very good, very proud
# not even saw theoratical solution