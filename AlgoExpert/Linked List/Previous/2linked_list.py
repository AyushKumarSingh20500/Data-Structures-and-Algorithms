class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def list_to_LL(l):  #Time: O(n) : n = number of elements in the list
    head = Node(l[0])
    curr = head
    for i in range(1, len(l)):
        new = Node(l[i])
        curr.next = new
        curr = new

    return head

def printLL(head): #Time = O(n) : n = size of the linked list
    while head:
        print(head.value, end=" ")
        head = head.next

def reverseLL(head): #Time = O(n) : n = size of the linked list
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev

def length_of_LL(head): #Time = O(n) : n = size of the linked list
    length = 0
    while head:
        length += 1
        head = head.next

    return length

def print_ith_node(head, idx): #Time: O(n) : n=idx
    curr = head
    for i in range(idx):
        curr = curr.next

    return curr.value

def delete_node_rec(head, idx):
    if(head == None):
        return 

    if(idx == 0):
        temp = head.next
        return temp

    head.next =  delete_node_rec(head.next, idx-1)
    return head

def swap_kth_from_start_and_end(head, k): #dont change pointer, change value
    head = head
    # prev = None
    curr = head
    for i in range(1, k):
        # prev = curr
        curr = curr.next

    # last = None
    laster = head
    for j in range(1, (length_of_LL(head)-k)+1):
        # last = laster
        laster = laster.next

    # temp = curr.next

    # prev.next = last
    # last.next = temp
    # temp.next = curr
    # curr.next = laster

    curr.value, laster.value = laster.value, curr.value

    return head


def find_a_node(head, value):
    count = 0
    while head:
        if(head.value == value):
            return count
        count += 1
        head = head.next

    return -1

def palindromeLL(head):
    head1 = head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    head2 = slow.next
    slow.next = None

    rev_head2 = reverseLL(head2)

    while rev_head2:
        if(head1.value != rev_head2.value):
            return False
        head1 = head1.next
        rev_head2 = rev_head2.next

    return True

def removeDuplicateLL(head):
    head = head
    curr1 = head
    curr2 = head.next
    while curr2 is not None:
        if(curr1.value == curr2.value):
            # if(newhead == None):
                # newhead = head
            # else:
                # newhead.next = head
            # head.next = curr1
            curr2 = curr2.next
        else:
            curr1.next = curr2
            curr1 = curr2
            curr2 = curr2.next
            # if(newhead == None):
                # newhead = head
            # else:
                # newhead.next = head
        curr2 = curr2.next

    return head


def insert_Ith(head, idx, value):
    curr = head
    for i in range(idx):
        curr = curr.next

    new = Node(value)
    temp = curr.next
    new.next = temp
    curr.next = new

    return head

    
def rotateLL(head, k):
    if(head == None or head.next==None or k==0):
        return head

    curr1 = head
    curr2 = head

    length = 1
    while curr2.next:
        length+=1
        curr2 = curr2.next

    curr2.next = head

    k = k % length
    k = length - k
    for i in range(1, k):
        curr1 = curr1.next

    head = curr1.next
    curr1.next = None

    return head

head = list_to_LL([1,2,3,4,5])
printLL(head)

print("")

# rev_head = reverseLL(head)
# printLL(rev_head)

print("")

# print(length_of_LL(head))

print("")

# print(print_ith_node(head, -1))

# del_head = delete_node_rec(head, 4)
# printLL(del_head)

# swaped_head = swap_kth_from_start_and_end(head, 4)
# printLL(swaped_head)

print("")

# print(length_of_LL(head))

# print(find_a_node(head, 9))

# print(palindromeLL(head))
# duphead = removeDuplicateLL(head)
# printLL(duphead)

# inserted = insert_Ith(head, 5, "new")

# printLL(inserted)

rotated = rotateLL(head, 6)
printLL(rotated)