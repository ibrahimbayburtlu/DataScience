class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None

class SLinkedList:
   def __init__(self):
      self.head = None

# Function to add node
   def inbetween(self,middle_node,newdata):
      if middle_node is None:
         print("The mentioned node is absent")
         return

      newnode = Node(newdata)
      newnode.next = middle_node.next
      middle_node.next = newnode

# Print the linked list
   def listprint(self):
      printval = self.head
      while printval is not None:
         print (printval.data)
         printval = printval.next

list = SLinkedList()
list.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thu")

list.head.next = e2
e2.next = e3

list.inbetween(list.head.next,"Fri")

list.listprint()