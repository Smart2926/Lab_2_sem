class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    def inorder_successor(node):
        if node.right:
            successor = node.right
            while successor.left:
                successor = successor.left
            return successor
        successor = node.parent
        while successor and node == successor.right:
            node = successor
            successor = successor.parent
        return successor
    
    first_successor = inorder_successor(node)
    if not first_successor:
        return None
    
    second_successor = inorder_successor(first_successor)
    return second_successor

def read_tree_from_file(filename):
    nodes = {}
    root = None
    level_nodes = []
    
    with open(filename, "r") as file:
        for line in file:
            values = line.strip().split()
            level_nodes.append([int(v) if v != "None" else None for v in values])
    
    if not level_nodes:
        return None
    
    root = BinaryTree(level_nodes[0][0])
    nodes[root.value] = root
    
    for i in range(len(level_nodes) - 1):
        current_level = level_nodes[i]
        next_level = level_nodes[i + 1]
        
        index = 0
        for value in current_level:
            if value is not None:
                node = nodes[value]
                if index < len(next_level) and next_level[index] is not None:
                    node.left = BinaryTree(next_level[index], parent=node)
                    nodes[next_level[index]] = node.left
                index += 1
                if index < len(next_level) and next_level[index] is not None:
                    node.right = BinaryTree(next_level[index], parent=node)
                    nodes[next_level[index]] = node.right
                index += 1
    
    return root

def print_tree_pyramid(root):
    from collections import deque
    if not root:
        return
    
    queue = deque([(root, 0)])
    levels = {}
    
    while queue:
        node, level = queue.popleft()
        if level not in levels:
            levels[level] = []
        levels[level].append(str(node.value) if node else " ")
        
        if node:
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
    
    max_width = len(" ".join(levels[max(levels.keys())]))
    
    for level in sorted(levels.keys()):
        row = " ".join(levels[level])
        print(row.center(max_width))

filename = "tree.txt"
tree = read_tree_from_file(filename)
print_tree_pyramid(tree)
