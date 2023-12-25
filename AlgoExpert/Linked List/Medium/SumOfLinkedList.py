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

head1 = list_to_LinkedList([2,4,7,1])
head2 = list_to_LinkedList([9,4,5])

def print_LinkedList(head):
    while head:
        print(head.value,end="-->")
        head = head.next
    print("None")

print_LinkedList(head1)
print_LinkedList(head2)

def sum_LinkedList(head1,head2):
    result = []
    carry = 0
    while head1 or head2:
        value1 = head1.value if head1 else 0
        value2 = head2.value if head2 else 0
        
        currentSum = carry + value1 + value2
        
        mod = currentSum // 10
        digit = currentSum % 10
        
        result.append(digit)
        
        if mod:
            carry = carry + mod
        else:
            carry = 0
            
        if head1:
            head1 = head1.next
            
        if head2:
            head2 = head2.next
            
    return list_to_LinkedList(result)

sum_LinkedListHead = sum_LinkedList(head1,head2)

print_LinkedList(sum_LinkedListHead)

# by me, without looking, very good, very proud
# not even saw theoratical solution