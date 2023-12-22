# class Node:  #created Node class, converted list to linked list, printed ll, reversed ll.
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# def list_to_LL(l):
#     head = Node(l[0])
#     curr = head
#     for i in range(1, len(l)):
#         new = Node(l[i])
#         curr.next = new
#         curr = new

#     return head

# list_head = list_to_LL(['a', 'b', 'c', 'd', 'e'])

# def printLL(head):
#     while head:
#         print(head.value, end=" ")
#         head = head.next
#     # print("None")

# printLL(list_head)

# print("")

# def print_nth(head, idx):
#     curr = head
#     for i in range(idx):
#         if(curr.next is not None): #makes sure that index is in range
#             curr = curr.next
#         else:
#             print("out of range")
#             return

#     # return curr.value
#     print(curr.value)

# print_nth(list_head, 2)


# def reverseLL(head):
#     prev = None
#     curr = head
#     while curr:
#         temp = curr.next
#         curr.next = prev
#         prev = curr
#         curr = temp

#     return prev

# rev_head = reverseLL(list_head)

# printLL(rev_head)

########################################################

# class Node:  #created Node class, converted list to linked list, printed ll, OOP way.
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class Linked_List:
    
#     def listToLL(self, l):
#         head = Node(l[0])
#         curr = head
#         for i in range(1, len(l)):
#             new = Node(l[i])
#             curr.next = new
#             curr = new

#         return head

#     def printLL(self, head):
#         while head:
#             print(head.value, end=" ")
#             head = head.next

# ll = Linked_List()
# ll_head = ll.listToLL([1,2,3,4,5])
# ll.printLL(ll_head)

#############################################

#  OOP Exercise

# class Vehicle:
#     color = "white"
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

#     # def max_capacity(self, capacity):
#     #     return f"{self.name}'s capacity is {capacity}"

#     def fare(self):
#         return self.capacity * 100

# class Bus(Vehicle):
    
#     # def max_capacity(self, capacity=50):
#     #     return super().max_capacity(capacity)

#     def fare(self):
#         total_fare = super().fare()
#         charge = 0.1 * total_fare
#         final_amount = total_fare + charge
#         return final_amount

# # class Car(Vehicle):
# #     pass

# # b1 = Bus("volvo", 80, 40)
# # print(b1.name)
# # print(b1.max_speed)
# # print(b1.mileage)
# # print(b1.max_capacity())
# # print(b1.color)

# # c1 = Car("audi", 260, 80)
# # print(c1.color)

# b2 = Bus("valvo", 80, 50)
# print(b2.fare())

# print(type(b2))

# print(isinstance(b2, Bus))
# print(isinstance(b2, Vehicle))

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next  = None


# class Linked_List:
#     def __init__(self):
#         self.head = None

#     def list_to_LL(self, l):
#         self.head = Node(l[0])
#         curr = self.head
#         for i in range(1, len(l)):
#             new = Node(l[i])
#             curr.next = new
#             curr = new

#         return self.head

#     def printLL(self, head):
#         while head:
#             print(head.value, end=" ")
#             head = head.next
    
#     # def deleteLL(self, head, idx): #not perfect
#     #     head = head
#     #     prev = Node(None)
#     #     curr = head
#     #     for i in range(idx):
#     #         temp = curr
#     #         curr = curr.next
#     #         prev = temp

#     #     temp2 = curr.next
#     #     prev.next = temp2

#     #     return temp2
    
#     def printMiddle(self, head):
#         slow = head
#         fast = head
#         while fast.next:
#             slow = slow.next
#             fast = fast.next.next

#         print(slow.value)

#     def insertIth(self, head, idx, value):
#         head = head
#         curr = head
#         if(idx!=0):
#             for i in range(idx-1):
#                 curr = curr.next

#             new = Node(value)
#             new.next = curr.next
#             curr.next = new
#         else:
#             new = Node(value)
#             new.next = curr
#             head = new

#         return head

# l = Linked_List()
# llhead = l.list_to_LL([1,2,3,4,5,6])
# l.printLL(llhead)
# print(" ")
# # dhead = l.deleteLL(llhead, 3)
# # l.printLL(dhead)
# # l.printMiddle(llhead)
# newhead = l.insertIth(llhead, 4, "three")
# l.printLL(newhead)



# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# def list_to_LL(l):
#     head = Node(l[0])
#     curr = head
#     for i in range(1, len(l)):
#         new = Node(l[i])
#         curr.next = new
#         curr = new

#     return head

# def middle_LL(head):
#     head = head
#     slow = head
#     fast = head
#     head1 = head
#     while fast.next is not None:
#         slow = slow.next
#         fast = fast.next.next

#     head2 = slow.next
#     slow.next = None

#     rev_head = reverse_LL(head2)

#     while rev_head is not None:
#         temp1 = head1.next
#         temp2 = rev_head.next

#         head1.next = rev_head
#         rev_head.next = temp1

#         head1 = temp1
#         rev_head = temp2

#     return head

# def reverse_LL(head):
#     prev = None
#     curr = head
#     while curr:
#         temp = curr.next
#         curr.next = prev
#         prev = curr
#         curr = temp

#     return prev

# def print_LL(head):
#     while head:
#         print(head.value, end=" ")
#         head = head.next

# head = list_to_LL([1,2,3,6,7,8,9])

# middle = middle_LL(head)

# print_LL(middle)


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None 

# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
# e = Node(5)
# f = Node(6)

# a.right = b
# b.right = c
# c.right = d
# d.right = e
# e.right = f

# def print_tree(root):
#     if(root == None):
#         return
#     print(root.value, end=":")
#     if(root.left != None):
#         print("l-", root.left.value, end=",")
#     if(root.right != None):
#         print("r-", root.right.value, end="")
#     print("")
#     print_tree(root.left)
#     print_tree(root.right)

# print_tree(a)















class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# def branch_sum(root, current_sum=0, array=[]):
#     if(root == None):
#         return

#     current_sum = current_sum + root.value

#     if(root.left == None and root.right == None):
#         array.append(current_sum)
#         return array

#     branch_sum(root.left, current_sum, array)
#     branch_sum(root.right, current_sum, array)

#     return array



# n1 = Node(1)
# n1.left = Node(2)
# n1.right = Node(3)
# n1.left.left = Node(4)
# n1.left.right = Node(5)
# n1.right.left = Node(6)
# n1.right.right = Node(7)
# n1.left.left.left = Node(8)
# n1.left.left.right = Node(9)
# n1.left.right.left = Node(10)
# n1.left.right.left.right = Node(1)


# print(branch_sum(n1))


