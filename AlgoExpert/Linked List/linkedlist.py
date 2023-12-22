# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)

# a.next = b
# b.next = c
# c.next = d

# print(c.next.value)

# //////////////////////////////////

# class Node: #detect cycle in a linked list
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# def cycle_check(head):
#     marker1 = head
#     marker2 = head

#     while marker2 != None and marker2.next != None:
#         marker1 = marker1.next
#         marker2 = marker2.next.next

#         if marker1 == marker2:
#             return True

#     return False

# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
# e = Node(5)

# a.next = b
# b.next = c
# c.next = d
# d.next = e

# print(cycle_check(a))

# /////////////////////////////////


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# def list_to_linked_list(mylist):
#     if(len(mylist) == 0):
#         return None

#     head = Node(mylist[0])
#     tail = head
#     for i in range(1, len(mylist)):
#         newNode = Node(mylist[i])
#         tail.next = newNode
#         tail = newNode

#     return head

# ll_head = list_to_linked_list([1,2,3,4,5])

# def print_linked_list(head):
#     while head:
#         print(head.value, end=" ")
#         head = head.next

# print_linked_list(ll_head)

# print("")

# def reverse_linked_list(head):
#     prev = None
#     curr = head
#     while curr:
#         temp = curr.next
#         curr.next = prev
#         prev = curr
#         curr = temp

#     return prev

# reversed_head = reverse_linked_list(ll_head)

# print_linked_list(reversed_head)

# ///////////////////////////////////

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# def list_to_ll(anList):
#     if(len(anList) == 0):
#         return None

#     head = Node(anList[0])
#     tail = head
#     for i in range(1, len(anList)):
#         newNode = Node(anList[i])
#         tail.next = newNode
#         tail = newNode

#     return head

# ll_head = list_to_ll([1,2,3,4,5,6,7,8])

# def print_LL(head):
#     while head:
#         print(head.value, end=" ")
#         head = head.next

# print_LL(ll_head)

# print("")

# def print_to_nth(head, n):
#     slow = head
#     fast = head
#     for i in range(n):
#         fast = fast.next

#     while fast != None and fast.next != None:
#         slow = slow.next
#         fast = fast.next

#     return slow.next.value

# print(print_to_nth(ll_head, 0))

# ///////////// Coding Ninjas Material //////////

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# def list_to_ll(mylist):
#     if(len(mylist) == 0):
#         return None
    
#     head = Node(mylist[0])
#     tail = head
#     for i in range(1, len(mylist)):
#         newNode = Node(mylist[i])
#         tail.next = newNode
#         tail = newNode

#     return head

# ll_head = list_to_ll([1,2,3,3,2,1])

# def print_ll(head):
#     while head:
#         print(head.value, end="-->")
#         head = head.next
#     print("none")

# print_ll(ll_head)

# print("")

# def reverse_ll(head):
#     prev = None
#     curr = head
#     while curr:
#         temp = curr.next
#         curr.next = prev
#         prev = curr
#         curr = temp

#     return prev

# reversed_head = reverse_ll(ll_head)

# print_ll(reversed_head)


# def print_ith_in_ll(head, idx):
#     curr = head
#     for i in range(idx):
#         curr = curr.next

#     return curr.value

# print(print_ith_in_ll(ll_head, 5))

# def length_of_ll(head):
#     count = 0
#     while head:
#         count = count + 1
#         head = head.next

#     return count

# print(length_of_ll(ll_head))


# def insert_in_ll(head, idx, value):
#     prev = None
#     curr = head
#     for i in range(idx):
#         prev = curr
#         curr = curr.next

#     newNode = Node(value)

#     prev.next = newNode
#     newNode.next = curr

#     return head

# new_LL = insert_in_ll(ll_head, 2, 99)

# print_ll(new_LL)

# def delete_in_ll(head, idx):
#     prev = None
#     curr = head
#     for i in range(idx):
#         prev = curr
#         curr = curr.next

#     temp = curr.next

#     prev.next = temp

#     return head

# del_ll = delete_in_ll(ll_head, 2)

# print_ll(del_ll)

# def search_ll(head, item):
#     while head:
#         if(head.value == item):
#             return True
#         else:
#             head = head.next

#     return False

# print(search_ll(ll_head, 8))

# def rotate_ll(head, idx):
#     prev = head
#     curr = head
#     head1 = head
#     for i in range(idx):
#         curr = curr.next

#     while curr.next != None:
#         prev = prev.next
#         curr = curr.next

#     head2 = prev.next
#     curr.next = head1
#     prev.next = None

#     return head2

# rotated = rotate_ll(ll_head, 4)

# print_ll(rotated)

# def remove_duplicated(head):
#     curr = head
#     while head and head.next:
#         if(head.value == head.next.value):
#             if(head.next.next != None):
#                 head.next = head.next.next
#             else:
#                 head.next = None
#         else:
#             head = head.next

#     return curr

# removed = remove_duplicated(ll_head)

# print_ll(removed)

# def remove_duplicates(head):
#     curr = head
#     while head and head.next:
#         if(head.value == head.next.value):
#             if(head.next.next != None):
#                 head.next = head.next.next
#             else:
#                 head.next = None
#         else:
#             head = head.next
    
#     return curr

# re = remove_duplicates(ll_head)
# print_ll(re)

# def palindrome_LL(head):
#     curr1 = head
#     curr2 = head
#     slow = head
#     fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next

#     curr2 = slow.next
#     slow.next = None

#     rev_curr2 = reverse(curr2)

#     while curr1 and rev_curr2:
#         if(curr1.value != rev_curr2.value):
#             return False
#         else:
#             curr1 = curr1.next
#             rev_curr2 = rev_curr2.next

#     return True


# def reverse(head):
#     prev = None
#     curr = head
#     while curr:
#         temp = curr.next
#         curr.next = prev
#         prev = curr
#         curr = temp

#     return prev

# print(palindrome_LL(ll_head))

# /////////////////////////////
# merge two sorted linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def listToLl(array):
    if(len(array) == 0):
        return None

    head = Node(array[0])
    tail = head
    for i in range(1, len(array)):
        newNode = Node(array[i])
        tail.next = newNode
        tail = newNode

    return head

# head1 = listToLl([0,2,4,6,8])
# head2 = listToLl([1,3,5,7,9])

# mhead1 = listToLl([0,2,4,6,8])
# mhead2 = listToLl([1,3,5,7,9])

# oddevenKLiaHead = listToLl([0,1,2,3,4,5,6,7,8,9])

llHead = listToLl([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

def printLl(head):
    while head:
        print(head.value, end="-->")
        head = head.next
    print("None")

# printLl(head1)
# # print("")
# printLl(head2)

printLl(llHead)

# def mergeSortedLl(head1, head2):
#     if head1 == None:
#         return head2
#     elif head2 == None:
#         return head1

#     finalHead = None
#     finalTail = None

#     if head1.value < head2.value:
#         finalHead = head1
#         finalTail = head1
#         head1 = head1.next
#     elif head2.value < head1.value:
#         finalHead = head2
#         finalTail = head2
#         head2 = head2.next

#     while head1 and head2:
#         if(head2.value < head1.value):
#             finalTail.next = head2
#             finalTail = head2
#             head2 = head2.next
#         elif(head1.value < head2.value):
#             finalTail.next = head1
#             finalTail = head1
#             head1 = head1.next

#     if head1 != None:
#         finalTail.next = head1
#     elif head2 != None:
#         finalTail.next = head2

#     return finalHead

# mergedLl = mergeSortedLl(mhead1, mhead2)

# printLl(mergedLl)

# ///////////////////////////////////////////

# def oddEven(head):
#     oddHead = None
#     oddTail = None
#     evenHead = None
#     evenTail = None

#     while head:
#         if(head.value % 2 == 0):
#             if(evenHead==None):
#                 evenHead = head
#                 evenTail = head
#             else:
#                 evenTail.next = head
#                 evenTail = head
#         elif head.value%2!=0:
#             if(oddHead==None):
#                 oddHead = head
#                 oddTail = head
#             else:
#                 oddTail.next = head
#                 oddTail = head

#         head = head.next
    
#     evenTail.next = None
#     oddTail.next = None
#     # oddTail.next = evenHead

#     oddTail.next = evenHead

#     return oddHead

# evenOddHead = oddEven(oddevenKLiaHead)

# printLl(evenOddHead)

# ////////////////////////////////////////

def n_and_m(head, n, m):
    prev = None
    curr = head
    temp = head
    while temp:
        for i in range(n):
            prev = curr
            curr = curr.next

        for j in range(m):
            if curr is not None:
                curr = curr.next
            else:
                break

        prev.next = curr

        temp = curr

    return head

nAndMHead = n_and_m(llHead, 3, 2)

printLl(nAndMHead)