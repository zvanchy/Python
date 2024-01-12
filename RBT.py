class Node:
    def __init__(self, key, color='RED'):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)
        self._insert_node(new_node)

    def _insert_node(self, node):
        # Perform regular BST insertion
        parent = None
        current = self.root
        while current is not None:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        # Fix any violations of the Red-Black Tree properties
        self._fix_insert(node)

    def _fix_insert(self, node):
        while node.parent is not None and node.parent.color == 'RED':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                if uncle is not None and uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)

                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left

                if uncle is not None and uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)

                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._rotate_left(node.parent.parent)

        self.root.color = 'BLACK'

    def delete(self, key):
        node = self._search(key)
        if node is None:
            return

        self._delete_node(node)

    def _delete_node(self, node):
        if node.left is None or node.right is None:
            y = node
        else:
            y = self._successor(node)

        if y.left is not None:
            x = y.left
        else:
            x = y.right

        if x is not None:
            x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        if y != node:
            node.key = y.key

        if y.color == 'BLACK':
            self._fix_delete(x)

    def _fix_delete(self, node):
        while node != self.root and (node is None or node.color == 'BLACK'):
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    node.parent.color = 'RED'
                    self._rotate_left(node.parent)
                    sibling = node.parent.right

                if (sibling.left is None or sibling.left.color == 'BLACK') and \
                        (sibling.right is None or sibling.right.color == 'BLACK'):
                    sibling.color = 'RED'
                    node = node.parent
                else:
                    if sibling.right is None or sibling.right.color == 'BLACK':
                        sibling.left.color = 'BLACK'
                        sibling.color = 'RED'
                        self._rotate_right(sibling)
                        sibling = node.parent.right

                    sibling.color = node.parent.color
                    node.parent.color = 'BLACK'
                    sibling.right.color = 'BLACK'
                    self._rotate_left(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    node.parent.color = 'RED'
                    self._rotate_right(node.parent)
                    sibling = node.parent.left

                if (sibling.left is None or sibling.left.color == 'BLACK') and \
                        (sibling.right is None or sibling.right.color == 'BLACK'):
                    sibling.color = 'RED'
                    node = node.parent
                else:
                    if sibling.left is None or sibling.left.color == 'BLACK':
                        sibling.right.color = 'BLACK'
                        sibling.color = 'RED'
                        self._rotate_left(sibling)
                        sibling = node.parent.left

                    sibling.color = node.parent.color
                    node.parent.color = 'BLACK'
                    sibling.left.color = 'BLACK'
                    self._rotate_right(node.parent)
                    node = self.root

        if node is not None:
            node.color = 'BLACK'

    def _search(self, key):
        node = self.root
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node
        return None
