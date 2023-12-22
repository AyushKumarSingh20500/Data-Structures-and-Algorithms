# # singly link list

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
# e = Node(5)

# a.next = b
# a.next.next = c

# print(a.value)
# print(a.next.next.value)

# -------------------------------------------------

# # doubly link list

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.prev = None

# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
# e = Node(5)

# a.next = b
# b.prev = a

# print(a.value)
# print(a.next.value)
# print(b.value)
# print(b.prev.value)

# -----------------------------------------

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# a = Node(1)         # jab node initialise karte hai to node.value = given value and node.next by default none set ho jata hai.
# b = Node(2)
# c = Node(3)
# d = Node(4)
# e = Node(5)

# a.next = b          # yaha p hum jo node.next by default none tha use overwrite kar rhe hai.
# b.next = c
# c.next = d
# d.next = c
# d.next = e

# # a.value = "ayush"      # here i tried overwriting nede.value and it worked.
# print(a.value)

# ------------------------------------------

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

#     def __str__(self):
#         node = self
#         output = ""
#         while node:
#             output += str(node.value) + " "
#             node = node.next
#         return output

# def list_to_LL(l):
#     if(len(l)==0):
#         return None
#     head = Node(l[0])
#     current = head
#     for i in range(1, len(l)):
#         # print(current.value)
#         new = Node(l[i])
#         current.next = new
#         current = current.next
#     return head

# n1 = list_to_LL([1,2,3,4,5])

# print(n1)

# -------------------------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def list_to_LL(l):
    head = Node(l[0])
    # current = head
    tail = head
    # print(tail.value)
    # print(tail.next)
    for i in range(1, len(l)):
        newNode = Node(l[i])
        # current.next = newNode
        tail.next = newNode
        tail = newNode
        # current = current.next
    return head

head = list_to_LL([1,2,3,4,5])

def printLL(head):
    while head != None:
        print(head.value, end=" ")
        head = head.next

printLL(head)

# ---------------------------
# # # 1. linked list creation
# # # 2. list to linklist
# # # 3. print linklist
# # # 4. length of the linklist
# # # 5. linklist reversal

# # # by me without out looking the solution

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# def makeLL(l):
#     head = Node(l[0])
#     tail = head
#     for i in range(1, len(l)):
#         newNode = Node(l[i])
#         tail.next = newNode
#         tail = newNode
#     return head

# myLL = makeLL([1,2,3,4,5,6])

# def printLL(head):
#     while head:
#         print(str(head.value), end=" ")
#         head = head.next

# printLL(myLL)
# print("")

# # def lengthLL(head):
# #     counter = 0
# #     while head:
# #         counter += 1
# #         head = head.next
# #     print(f"length is {counter}")

# # # lengthLL(myLL)

# # def reverseLL(head):
# #     prev = None
# #     while head:
# #         temp = head.next
# #         head.next = prev
# #         prev = head
# #         head = temp
# #     return prev

# # rev = reverseLL(myLL)

# # # printLL(rev)
# # # print("")

# def pritn_ith(head, idx):
#     left = head
#     for i in range(idx):
#         if(left.next == None):
#             return
#         left = left.next
#     return left


# # printLL(myLL)
# # print("")

# ith = pritn_ith(myLL, 5)
# print(ith.value)


# # printLL(myLL)
# # print("")
# # lengthLL(head)
# # printLL(rev)

# ----------------------------------

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def makeLL(self, mylist):
#         head = Node(mylist[0])
#         current = head
#         for i in range(1, len(mylist)):
#             new = Node(mylist[i])
#             current.next = new
#             current = new
#         return head

#     # listHead = makeLL(self, [1,2,3,4,5])

#     def printLL(self, head):
#         while head:
#             print(head.value, end=" ")
#             head = head.next

#     def printMiddle(self, head):
#         slow = head
#         fast = head
#         while fast.next != None:           # while fast and fast.next != none
#             slow = slow.next
#             fast = fast.next.next

#         print(f"\nmid is {slow.value}")

#     def reverseLL(self, head):
#         prev = None
#         while head:
#             temp = head.next
#             head.next = prev
#             # head = temp
#             prev = head
#             head = temp
#         return prev

#     # def rotateLL(self, head, idx):
#     #     current = head
#     #     key = head
#     #     for i in range(idx):
#     #         key = key.next
#     #     key.next = None
#     #     while key:
#     #         key2 = key.next
#     #     key2.next = current
#     #     return 

#     def lengthLL(self, head):
#         counter = 0
#         while head:
#             counter += 1
#             head = head.next
#         return counter

#     def add_ith(self, head, idx, value):
#         if(idx<0 or idx>length):
#             return head

#         prev = None
#         curr = head
#         new = Node(value)

#         for i in range(idx):
#             prev = curr
#             curr = curr.next

#         if prev is not None:
#             prev.next = new
#         else:
#             head = new
#         new.next = curr

#         return head

#     def delete_ith(self, head, idx):
#         if(idx<0 or idx>length):
#             return head

#         prev = None
#         curr = head

#         for i in range(idx):
#             prev = curr
#             curr = curr.next

#         temp = curr.next
#         prev.next = temp

#         return head

#     def add_ith_recursive(self, head, idx, value):
#         if(idx<0 or idx>length):
#             raise("List index out of range")

#         new = Node(value)

#         if(idx==0):
#             new.next = head
#             head = new
#             return head

#         smallhead = ll.add_ith_recursive(head.next, idx-1, value)
#         head.next = smallhead
#         return head



# ll = LinkedList()


# head = ll.makeLL([1,2,3,4,5])
# ll.printLL(head)

# length = ll.lengthLL(head)

# # print(ll.lengthLL(head))
# print("")

# # new_head = ll.add_ith(head, 3, "ayush")

# addrec = ll.add_ith_recursive(head, 5, "sachin")
# ll.printLL(addrec)




# # ll.printLL(new_head)
# # print("")

# # del_head = ll.delete_ith(head, 3)
# # ll.printLL(del_head)

# # ll.printMiddle(head)

# # tail = ll.reverseLL(head)
# # ll.printLL(tail)

# # ll.printMiddle(tail)

# -----------------------------------

#  merge linked list :  not completed

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# def makeLL(mylist):
#     head = Node(mylist[0])
#     current = head
#     for i in range(1, len(mylist)):
#         new = Node(mylist[i])
#         current.next = new
#         current = new
#     return head

# list1 = makeLL([1,3,5,7,9])
# list2 = makeLL([2,4,6,8,10])

# def printLL(head):
#     while head:
#         print(head.value, end=" ")
#         head = head.next

# printLL(list1)
# print("")
# printLL(list2)

# def mergeLL(head1, head2):
#     finalHead = None
#     finalTail = None

#     if(head1.value<head2.value):
#         finalHead = head1
#         finalTail = head1
#     else:
#         finalHead = head2
#         finalTail = head2

#     head1 = head1.next
    

# -----------------------------------

#  stack problem

# def check_redundant(s):                     # by me without looking the solution
#     pairs = {"]":"[", "}":"{", ")":"("}
#     closing = "}])"
#     opening = "{[("
#     mystack = []
#     for i in s:
#         if(i not in closing):
#             mystack.append(i)
#             count = 0
#             print(mystack)
#         else:
#             last = mystack[-1]
#             print(last)
#             count = 0
#             print(count)
#             while last != pairs[i]:
#                 mystack.pop()
#                 print(mystack)
#                 count += 1
#                 last = mystack[-1]
#                 print(last)
#                 print(count)
#             mystack.pop()


#     # if(count == 0):
#     #     return "Redundant"
#     # else:
#     #     return "Not redundant"

#     # return count == 0

#     return "redundant" if(count==0) else "not redundant"

# print(check_redundant("(a+(a+b))"))

# ----------------------------------------------




























































































# -----------------------------------------------Link list starting again ------------------------------

# # singly linklist , doubly link list, circular link list

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# a = Node("a")
# b = Node("b")
# c = Node(3)
# d = Node("e")

# a.next = b
# b.next = c
# c.next = d

# print(a.value)
# print(a.next.value)

# print(a.next.next.value)

# -------------------------------------------------

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# def makeLL(l):
#     if(len(l)==0):
#         return 
#     head = Node(l[0])
#     curr = head
#     for i in range(1, len(l)):
#         new = Node(l[i])
#         curr.next = new
#         curr = new

#     return head

# head = makeLL([1,2,3,4,5])

# def printLL(head):
#     while head:
#         print(head.value, end=" ")
#         head = head.next
#     # print("None")
#     print("")

# printLL(head)

# def lengthLL(head):
#     counter = 0
#     while head:
#         counter += 1
#         head = head.next
#     return counter

# print(lengthLL(head))

# # def reverseLL(head):
# #     prev = None
# #     while head:
# #         temp = head.next
# #         head.next = prev
# #         prev = head
# #         head = temp

# #     return prev

# # rev_head = reverseLL(head)

# # printLL(rev_head)

# def add_ith(head, idx, value):
#     if(idx<0 or idx>5):
#         return head

#     prev = None
#     curr = head

#     new = Node(value)

#     for i in range(idx):
#         prev = curr
#         curr = curr.next

#     if(prev is not None):
#         prev.next = new
#     else:
#         head = new
#     new.next = curr

#     return head

# ith = add_ith(head, 5, "new")
# jth = add_ith(head, 0, "new value")

# # printLL(head)

# printLL(ith)
# # print("")
# printLL(jth)

# --------------------------------------------

# class Node:                          # Tip do not implement linked list as class 
#     def __init__(self, value):       # things will get complicated
#         self.value = value
#         self.next = None

# class LinkedList:
#     # def __init__(self):
#     #     self.value = None
#     #     self.next = None

#     def makeLL(self, mylist):
#         head = Node(mylist[0])
#         curr = head
#         for i in range(1, len(mylist)):
#             new = Node(mylist[i])
#             curr.next = new
#             curr = new
#         return head

#     def printLL(self, head):
#         while head:
#             print(head.value, end=" ")
#             head = head.next

#     def lengthLL(self, head):
#         counter = 0
#         while head:
#             counter += 1
#             head = head.next
#         return counter

#     def reverseLL(self, head):
#         prev = None
#         while head:
#             temp = head.next
#             head.next = prev
#             prev = head
#             head = temp
#         return prev

#     def add_ith(self,head, idx, value):
#         if(idx<0 and idx>self.counter):
#             return("index out of range")

#         prev = None
#         curr = head
#         new = Node(value)
#         for i in range(idx):
#             prev = curr
#             curr = curr.next

#         if(prev is not None):
#             prev.next = new
#         else:
#             head = new
#         new.next = curr

#         return head

#     def deleteLL(self,head, idx):
#         prev = None
#         curr = head
#         for i in range(idx):
#             prev = curr
#             curr = curr.next

#         temp = curr.next
#         prev.next = temp

#         return head



# LL = LinkedList()

# head = LL.makeLL([1,2,3,4,5])
# LL.printLL(head)
# print("")

# length = LL.lengthLL(head)
# print(length)

# # revHead = LL.reverseLL(head)
# # LL.printLL(revHead)

# added = LL.add_ith(head, 5, "new")
# LL.printLL(added)
# print("")

# revHead = LL.reverseLL(added)  #this one working fine
# LL.printLL(revHead)
# print("")

# deleted = LL.deleteLL(head, 0)
# LL.printLL(deleted)

# ---------------------------------

# # def sumOfTwo(a,b,v):
# #     for i in a:
# #         for j in b:
# #             if(i+j==v):
# #                 return [i, j]
# #     return False

# # a = [0,0,-5,30212]
# # b = [-10, 40, -3, 9]
# # print(sumOfTwo(a, b, -8))

# def sumOfTwo(a, b, v):
#     req = {}
#     for i in a:
#         req[v-i] = True

#     for j in b:
#         if(j in req.keys()):
#             return True

#     return False

# a = [0,0,-5,30212]
# b = [-10, 40, -3, 9]

# print(sumOfTwo(a, b, -8))

# ---------------------------------------

































































































# --------------------------------------------


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# def makeLL(mylist):
#     head = Node(mylist[0])
#     curr = head
#     for i in range(1, len(mylist)):
#         new = Node(mylist[i])
#         curr.next = new
#         curr = new

#     return head

# head = makeLL([3,0,5,2,1,4])

# head1 = makeLL([1])
# head2 = makeLL([2])

# def printLL(head):
#     while head:
#         print(head.value, end=" ")
#         head = head.next
#     # print("None")

# # printLL(head)
# # print("")

# def merge_even_odd(head):
#     # curr = head
#     oddHead = None
#     evenHead = None
#     # while curr != None:
#     while head:
#         if(head.value%2==0):
#             if(evenHead == None):
#                 evenHead = head
#                 evenTail = head
#             else:
#                 evenTail.next = head
#                 evenTail = head
#         else:
#             if(oddHead == None):
#                 oddHead = head
#                 oddTail = head
#             else:
#                 oddTail.next = head
#                 oddTail = head

#         head = head.next

#     evenTail.next = None
#     oddTail.next = evenHead

#     # oddTail.next = None
#     # evenTail.next = oddHead

#     return oddHead

# # odd_even = merge_even_odd(head)
# # printLL(odd_even)
# # print("")

# # -----------------------------------------------------------

# def n_and_m(head, n, m):         # solution by me without looking the solution. Good job.
#     prev = None
#     temp = head
#     curr = head
#     while temp:
#         for i in range(n):
#             # if(curr is not None):
#             prev = curr
#             curr = curr.next
#             # else:
#                 # break

#         for j in range(m):
#             if(curr is not None):
#                 curr = curr.next
#             else:
#                 break

#         prev.next = curr

#         temp = temp.next

#     return head

# # new_head = n_and_m(head, 1, 3)
# # printLL(new_head)
# # print("")

# # ---------------------------------------------

# def searchLL(head, value):   # Searches the linked list for a value and returns its index if present, else returns -1.
#     counter = 0               # By me without looking the solution
#     while head is not None:
#         if(head.value == value):
#             return counter
#         else:
#             head = head.next
#             counter += 1

#     return -1

# # print(searchLL(head,6))

# # ------------------------------------------------

# def rotate_clockwise(head, idx):     #By me without looking the solution
#     prev = None                 
#     start = head
#     curr = head

#     if(idx<0 or idx>9):
#         print("out of range")
#         # raise IndexError
#         return
#     if(idx == 0 or idx == 9):   # 9 is length of linklist, do not hard code it calculate length and then use it.
#         return start

#     for i in range(idx+1):
#         prev = curr
#         curr = curr.next

#     prev.next = None
#     new_head = curr

#     while curr.next:
#         curr = curr.next

#     curr.next = start

#     return new_head

# # rotated = rotate_clockwise(head, 2)
# # # print(rotated)
# # printLL(rotated)
# # print("")

# # -------------------------------------------------------

# def rearrangeLinkedList(head, k):         # by me without looking the solution.
#     curr = head
#     smallList = None
#     bigList = None
#     while curr is not None:
#         if(curr.value < k):
#             if(smallList == None):
#                 smallList = curr
#                 smallTail = curr
#             else:
#                 smallTail.next = curr
#                 smallTail = smallTail.next
#         elif(curr.value >= k):
#             if(bigList == None):
#                 bigList = curr
#                 bigTail = curr
#             else:
#                 bigTail.next = curr
#                 bigTail = bigTail.next

#         curr = curr.next

#     smallTail.next = bigList      # <---
#     bigTail.next = None           #    |  both working fine.
#     # smallTail.next = bigList    # <---



#     return smallList

# # rearranged = rearrangeLinkedList(head, 3)
# # printLL(rearranged)
# # print("")

# # -----------------------------------------------------

# def mergeLL(head1, head2):            # solution by me without looking the solution.
#     head = None
#     h1 = head1
#     h2 = head2
#     curr1 = head1
#     curr2 = head2

#     if(curr1.value < curr2.value):
#         head = h1
#     else:
#         head = h2

#     while curr1 is not None and curr2 is not None:
#         if(curr1.value < curr2.value):
#             temp = curr1.next
#             curr1.next = curr2
#             curr1 = temp
#         else:
#             temp = curr2.next
#             curr2.next = curr1
#             curr2 = temp

#     return head

# printLL(head1)
# print("")
# printLL(head2)
# print("")


# merged = mergeLL(head1, head2)
# printLL(merged)
# print("")


# def sum_LL(linkedlistOne, linkedlisttwo):
#     newLinkedList = Node(0)
#     curr =newLinkedList
#     carry = 0

#     head1 = linkedlistOne
#     head2 = linkedlisttwo
#     while head1 is not None or head2 is not None or carry != 0:
#         valueOne = head1.value if head1 is not None else 0
#         valuetwo = head2.value if head2 is not None else 0

#         sumofnodes = valueOne + valuetwo + carry

#         newvalue = sumofnodes%10
#         newnode = Node(newvalue)
#         curr.next = newnode
#         curr = newnode

#         carry = sumofnodes//10

#         head1 = head1.next if head1 is not None else None
#         head2 = head2.next if head2 is not None else None

#     return newLinkedList.next

# # summed = sum_LL(head1, head2)
# # printLL(summed)







# def twoNumberSum(myarray, total):
#     req = {}
#     for i in myarray:
#         if((total-i) in req.keys()):
#             return [i, total-i]
#         req[i] = True
    
#     return False

# myarray = [2,8]
# print(twoNumberSum(myarray, 10))


# z = [1,2,3].extend([1,2,3])
# print(z)