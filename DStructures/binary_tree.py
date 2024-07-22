from collections import deque

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    # Insert New Node Using Breadth First Insertion
    def insert_node(self, data) -> Node:
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        q = deque()
        q.append(self.root)
        while q:
            current = q.popleft()
            if current.left is None:
                current.left = new_node
                break
            else:
                q.append(current.left)

            if current.right is None:
                current.right = new_node
                break
            else:
                q.append(current.right)

        return self.root

    # Calc The Height    
    def height(self):
        return self.internal_height(self.root)

    # Recursive Function To Calc Height
    def internal_height(self, node):
        if node is None:
            return 0
        return 1 + max(self.internal_height(node.left), self.internal_height(node.right))
    
    def pre_order(self):
        return self.internal_pre_orded(self.root)

    def internal_pre_orded(self, node):
        if node is not None:
            print(node.data, "->" ,end=" ")
            self.internal_pre_orded(node.left)
            self.internal_pre_orded(node.right)

    def in_order(self):
        return self.internal_in_orded(self.root)

    def internal_in_orded(self, node):
        if node is not None:
            self.internal_in_orded(node.left)
            print(node.data, "->" ,end=" ")
            self.internal_in_orded(node.right)