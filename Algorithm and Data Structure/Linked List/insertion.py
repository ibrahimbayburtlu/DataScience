class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        listval = self.head
        while listval is not None:
            print(listval)
            listval = listval.next
    def atbeginning(self,newdata):
        newnode = Node(newdata)
        newnode.next = self.head
        self.head = newnode


list = SLinkedList()
list.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.head.next = e2
e2.next = e3

list.atbegining("Sun")
list.listprint()
