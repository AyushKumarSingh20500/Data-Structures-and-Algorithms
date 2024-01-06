class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def list_to_linkedList(array):
    if len(array) == 0:
        return None
    
    head = Node(array[0])
    tail = head
    for i in range(1,len(array)):
        newNode = Node(array[i])
        tail.next = newNode
        tail = newNode
        
    return head

head1 = list_to_linkedList([2,4,7,1])
head2 = list_to_linkedList([9,4,5])

def print_linkedList(head):
    while head:
        print(head.value,end="-->")
        head = head.next
    print("None")

print_linkedList(head1)
print_linkedList(head2)

def sumOfLinkedList(head1,head2):
    result = []
    carry = 0
    while head1 != None or head2 != None:
        value1 = head1.value if head1 != None else 0
        value2 = head2.value if head2 != None else 0
        
        currentSum = value1 + value2 + carry
        
        digit = currentSum % 10
        mod = currentSum // 10
        
        result.append(digit)
        
        if mod != 0:
            carry = mod
        else:
            carry = 0
            
        if head1 != None:
            head1 = head1.next
        if head2 != None:
            head2 = head2.next
        
    resultHead = list_to_linkedList(result)
    
    return resultHead

sumOfLinkedListHead = sumOfLinkedList(head1,head2)

print_linkedList(sumOfLinkedListHead)