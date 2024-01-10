'''
insert algorithm  
1, when tree is empty create a new node as root node with black colour
2. if tree is not empty creeate a new node as leaf node with red colour
3. if parent of new node is black then exit
4.a if parent of new node is red then we have to check the color of the parent's sibling
of new Node
a. if color is black, perform rotation and recolouring
b. if color is red, check if grandparent of new node is root, if not root recolour

'''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'RED'

class RedBlackTree:
    def __init__(self, key):
        self.root = None
        
    
    def insert(self, key):
        node  = Node(key)
        
        if self.root is None:
            self.root = node
            self.root.color = 'BLACK'
            return

        current = self.root
        parent = None
        
        while current is not None:
            parent = current
            
            if node.key < current.key:
                current = current.left
            else:
                current = current.right
            
        node.parent = parent
        
        if node.key < parent.key:
            parent.left = node
        else:
            parent.right = node
        
        self.fix_insert(node)
        
    def fix_insert(self, node):
        while node.parent and node.parent.color == 'RED':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                if uncle and uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)

                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left

                if uncle and uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)

                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.rotate_left(node.parent.parent)

        self.root.color = 'BLACK'       
                    