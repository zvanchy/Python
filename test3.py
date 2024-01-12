class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right  = None
        
    def getValue(self):
        return self.value

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)
        
    def _insert_recursive(self, node, key):
        
        if node is None:
            return Node(key)
        elif key < node.key :
            node.left = self._insert_recursive(node.left, key)
        else:
           
            node.right = self._insert_recursive(node.right, key)
        return node
    
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)
    
    def _delete_recursive(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key :
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp  = self._find_min_from_right(node.right)
                node.key = temp.key
                node.right = self._delete_recursive(node.right, temp.key)
        return node                    
    
    def _find_min_from_right(self,node):
        while node.left is not None:
            return node.left
        return node
    
    def inorder_traversal(self):
        return self._inorder_recursive(self.root)
    
    def _inorder_recursive(self, node):
        result = []
        if node :
            result = self._inorder_recursive(node.left)
            result.append(node.key)
            result += self._inorder_recursive(node.right)
        
        return result
    
tree = BinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)
print("Inorder Traversal:", tree.inorder_traversal())
tree.delete(80)
tree.insert(80)
print("Inorder Traversal:", tree.inorder_traversal())
    