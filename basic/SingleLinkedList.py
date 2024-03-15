class Node:
    def __init__(self, data, next1= None) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return 
    
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
        new_node.next = temp.next.next
    
    def print_nodes(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def delete_node(self, key):
        
        temp = self.head
        while temp.data != key:
            temp = temp.next
        temp.data = temp.next.data
        temp.next = temp.next.next
    

ll = LinkedList()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.add_node(4)
ll.add_node(5)
ll.add_node(6)
ll.add_node(7)
ll.print_nodes()
ll.delete_node(4)
ll.print_nodes()