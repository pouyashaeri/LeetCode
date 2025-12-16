from typing import Optional

class NodeList:
    def __init__(self, val):
        self.val = val
        self.next = None
   

l1 = NodeList(1)
l2 = NodeList(2)
l3 = NodeList(3)

l1.next = l2
l2.next = l3

##################################################

def print_linkedlist(l):
    print("Print LinkedList: ")
    cur = l
    while cur:
        print(cur.val)
        cur = cur.next
    return

# print_linkedlist(l1)

##################################################

def build_linkedlist(array):
    head = NodeList(array[0])
    cur = head
    for i in range(1, len(array)):
        cur.next = NodeList(array[i])
        cur = cur.next
    return head

l2 = build_linkedlist([3, 4, 2, 1])
print_linkedlist(l2)

##################################################

def build_array(l: Optional[NodeList]):
    arr = []
    cur = l
    while cur:
        arr.append(cur.val)
        cur = cur.next
    return arr

array = build_array(l2)
# print(array)

###################################################

def reverse_linkedlist(l: Optional[NodeList]):
    cur = l
    prev = None

    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node

    return prev

reverse_l2 = reverse_linkedlist(l2)

print_linkedlist(reverse_l2)