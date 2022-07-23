# Creation of Linked list
class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

list = LinkedList()
list.head = Node("Mon")
list2 = Node("Tue")
list3 = Node("Wed")

list.head.next = list2
list2.next = list3
