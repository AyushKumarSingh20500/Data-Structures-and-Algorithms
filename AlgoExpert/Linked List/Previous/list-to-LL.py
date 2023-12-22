class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def list_to_ll(mylist):
    if(len(mylist) == 0):
        return None

    head = Node(mylist[0])
    tail = head
    for i in range(1, len(mylist)):
        newNode = Node(mylist[i])
        tail.next = newNode
        tail = newNode

    return head

head = list_to_ll([1,2,3,4,5])

def print_ll(head):
    while head:
        print(head.value, end="-->")
        head = head.next
    print("None")

print_ll(head)