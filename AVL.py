import matplotlib.pyplot as plt
import networkx as nx
    
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)
        print("After inserting", key)
        print("Height of root:", self.root.height)
        print("Balance factor:", self.get_balance_factor(self.root))
        print("Tree structure:")
        # self.visualize_avl_tree()  # Print tree structure
        
        
    def _insert_recursive(self, root, key):
        if not root:
            return Node(key)
        
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        else:
            root.right = self._insert_recursive(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        balance = self.get_balance_factor(root)
        
        # Left-Left rotation case
        if balance > 1 and key < root.left.key:
            return self.right_rotation(root)

        # Right-Right rotation case
        if balance < -1 and key > root.right.key:
            return self.left_rotation(root)

        # Left-Right rotation case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)

        # Right-Left rotation case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotation(root.right)
            return self.left_rotation(root)

        return root
    
    def left_rotation(self, y):
        x = y.right
        temp = x.left
        x.left = y
        y.right = temp
        
        x.height = 1 + max(self.get_height(x.left),self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return x
    
    def right_rotation(self, x):   
        y = x.left
        temp = y.right
        y.right = x
        x.left = temp
        
        x.height = 1 + max(self.get_height(x.left),self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return y
        
    
                    
    def get_height(self, node):
        if node is None:
            return 0 
        else:
            return node.height   
    
    def get_balance_factor(self, node):
        if node is None:
            return 0
        else:
            return self.get_height(node.left) - self.get_height(node.right)
        
    def traverse(self):
        self.display_tree(self.root)
        return self._inorder_recursive(self.root)
    
    def _inorder_recursive(self, node):
        result = []
        if node:
            result = self._inorder_recursive(node.left)
            result.append(node.key)
            result += self._inorder_recursive(node.right)
        return result
    
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)
        print("After deleting", key)
        print("Tree structure:")
        # self.visualize_avl_tree()  # Print tree structure
        print("Height of root:", self.root.height)
        print("Balance factor:", self.get_balance_factor(self.root))
    
    def _delete_recursive(self, root, key):
        if root is None:
            return None
        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                temp = self._find_min(root.right)
                root.key = temp.key
                root.right = self._delete_recursive(root.right, temp.key)
                
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        
        
        balance_factor = self.get_balance_factor(root)
        
        
        if balance_factor > 1 and key < root.left.key:
            return self.right_rotation(root)
        
        if balance_factor < -1 and key > root.right.key:
            return self.left_rotation(root)
        
        if balance_factor > 1 and key > root.left.key:
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)
        
        if balance_factor < -1 and key < root.right.key:
            root.right = self.right_rotation(root.right)
            return self.left_rotation(root)
        
        print("After deleting", key)
        print("Tree structure:")
        # self.visualize_avl_tree()  # Print tree structure
        print("Height of root:", root.height)
        print("Balance factor:", balance_factor)
        return root
    
    def _find_min(self, node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node
    
    
    def traverse_avl_tree(self, node, graph):
        if node is None:
            return
    
        # Add the current node to the graph
        graph.add_node(node.key)
    
        if node.left is not None:
            # Add an edge between the current node and its left child
            graph.add_edge(node.key, node.left.key)
    
        if node.right is not None:
            # Add an edge between the current node and its right child
            graph.add_edge(node.key, node.right.key)
    
        # Recursively traverse the left and right subtrees
        self.traverse_avl_tree(node.left, graph)
        self.traverse_avl_tree(node.right, graph)
    
   
    def visualize_avl_tree(self):
        # Create an empty graph
        graph = nx.Graph()
    
        # Traverse the AVL tree and add nodes and edges to the graph
        self.traverse_avl_tree(self.root, graph)
    
        # Position the nodes in the graph
        pos = nx.nx_agraph.graphviz_layout(graph, prog="dot")
    
        # Draw the graph
        nx.draw(graph, pos, with_labels=True, node_size=800, node_color='lightblue', font_size=12, font_weight='bold', edge_color='gray')
    
        # Display the graph
        plt.show()
    
    def display_tree(self, root, level=0, prefix='Root: ', indent='   '):
        if root is not None:
            if level == 0:
                print(prefix + str(self.root.key))
            else:
                print(indent * (level - 1) + '|___' + str(root.key))
            if self.root.left is not None or self.root.right is not None:
                self.display_tree(root.left, level + 1, 'L:', indent)
                self.display_tree(root.right, level + 1, 'R:', indent)
    
    
    def is_balanced(self):
        return self._is_balanced(self.root)

    def _is_balanced(self, node):
        if not node:
            return True

        balance = self.get_balance_factor(node)

        if abs(balance) > 1:
            return False

        return self._is_balanced(node.left) and self._is_balanced(node.right)
    
avl_tree = AVL()

# Insert nodes to test balancing
avl_tree.insert(33)
avl_tree.insert(13)
avl_tree.insert(52)
avl_tree.insert(9)
avl_tree.insert(21)
avl_tree.insert(61)
avl_tree.insert(8)
avl_tree.insert(11)
avl_tree.visualize_avl_tree()
is_balanced = avl_tree.is_balanced()
print("Is AVL tree balanced?", is_balanced)



# avl_tree.visualize_avl_tree()
# is_balanced = avl_tree.is_balanced()
# print("Is AVL tree balanced?", is_balanced)

avl_tree.delete(13)
avl_tree.visualize_avl_tree()

avl_tree.insert(45)
avl_tree.visualize_avl_tree()

avl_tree.delete(30)
avl_tree.visualize_avl_tree()

avl_tree.delete(35)
avl_tree.visualize_avl_tree()

avl_tree.delete(40)
avl_tree.visualize_avl_tree()

avl_tree.insert(60)
avl_tree.visualize_avl_tree()

avl_tree.insert(70)
avl_tree.visualize_avl_tree()

avl_tree.insert(80)
avl_tree.visualize_avl_tree()

# Additional operations, rotations, etc., to check the AVL property

# Check if the tree remains balanced (use AVL property checks)
is_balanced = avl_tree.is_balanced()
print("Is AVL tree balanced?", is_balanced)


