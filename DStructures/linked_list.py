# Node Class Implementation
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# List Class Implementaion
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def count_list(self) -> int:
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def insert_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    
    def insert_after(self, node, data):
        current_node, parent_node = self.find_node_data(node)
        if self.head is not None and current_node is not None:
           new_node = Node(data) 

           new_node.next = current_node.next
           parent_node.next = new_node
        
        if current_node is None:
            self.insert_node(data)
            return
    
    def delete_head(self):
        if self.head is not None:
            self.head = self.head.next
            return
    
    def delete_node(self, node):
        node_to_deleted, parent_node = self.find_node_data(node)

        if self.head is node_to_deleted:
            self.delete_head()
        else:
            if node_to_deleted.next is None:
                parent_node.next = None
            else:
                parent_node.next = node_to_deleted.next

    # def find_node(self, data):
    #     if self.head is None:
    #         return
        
    #     current = self.head
    #     while current:
    #         if current.data == data:
    #             return current
    #         current = current.next
    #     return None
    
    # def find_parent(self, data):
    #     if self.head is None:
    #         return
        
    #     current = self.head
    #     while current:
    #         if current.next.data == data:
    #             return current
    #         current = current.next
    #     return None

    def find_node_data(self, data) -> Node:
        current = self.head
        prev = None

        while current:
            if current.data == data:
                return current, prev
            prev = current
            current = current.next

        return None, prev

