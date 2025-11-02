class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next     # temporarily save next node
            current.next = prev    # reverse the link
            prev = current         # move prev forward
            current = nxt          # move current forward
        self.head = prev           # update head to last node

# Examples:
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

print("The created Linked list:")
ll.display()

ll.reverse()
print("Reversed list:")
ll.display()