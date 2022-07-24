class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def yazdir(self):
        printval = self.head
        
        while printval is not None:
            print(printval.data)
            printval = printval.next
list = LinkedList()
e1 = Node(1)
list.head = e1
e2 = Node(2)
e3 = Node(3)
e1.next = e2
e2.next = e3

list.yazdir()

