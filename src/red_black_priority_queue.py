class Node:
    def __init__(self, value, priority, color='red'):
        self.value = value
        self.priority = priority
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackPriorityQueue:
    def __init__(self):
        self.NIL = Node(None, float('-inf'), color='black')
        self.root = self.NIL

    def insert(self, value, priority):
        new_node = Node(value, priority)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if priority > current.priority:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if not parent:
            self.root = new_node
        elif priority > parent.priority:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'red'
        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node.parent and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)
        self.root.color = 'black'

    def left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left != self.NIL:
            right_child.left.parent = node
        right_child.parent = node.parent
        if not node.parent:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right != self.NIL:
            left_child.right.parent = node
        left_child.parent = node.parent
        if not node.parent:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def extract_max(self):
        if self.root == self.NIL:
            return None
        max_node = self.find_max(self.root)
        self.delete_node(max_node)
        return max_node.value

    def find_max(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def delete_node(self, node):
        if node.left == self.NIL and node.right == self.NIL:
            if node == self.root:
                self.root = self.NIL
            elif node == node.parent.left:
                node.parent.left = self.NIL
            else:
                node.parent.right = self.NIL
        elif node.left == self.NIL:
            self.transplant(node, node.right)
        elif node.right == self.NIL:
            self.transplant(node, node.left)
        else:
            successor = self.find_max(node.right)
            node.value, node.priority = successor.value, successor.priority
            self.delete_node(successor)

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def peek_max(self):
        if self.root == self.NIL:
            return None
        return self.find_max(self.root).value

    def inorder_traversal(self, node):
        if node != self.NIL:
            self.inorder_traversal(node.left)
            print(f'Value: {node.value}, Priority: {node.priority}, Color: {node.color}')
            self.inorder_traversal(node.right)

    def display(self):
        self.inorder_traversal(self.root)

A = RedBlackPriorityQueue()
A.insert("1", 10)
A.insert("2", 20)
A.insert("3", 5)
A.insert("4", 15)
A.insert("5", 25)
print("Queue after insertions:")
A.display()

print("Delete", A.extract_max())
print("Queue after delete:")
A.display()

print("Peeking max:", A.peek_max())
