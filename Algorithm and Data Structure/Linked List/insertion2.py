class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
    
    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def atbeginning(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def atend(self,data=None):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return   
        last = self.head
        while (last.next):
            last = last.next
        last.next = newnode
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)

list = SLinkedList()
list.head = e1
e1.next = e2
e2.next = e3

list.atbeginning(0)
list.atend(4)
list.listprint()