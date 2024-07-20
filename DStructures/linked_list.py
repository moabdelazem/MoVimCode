# Node Class Impelmentation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Iterator Class
class ListIterator:
    def __init__(self, node = None) -> None:
        self.current = node
    
    # Return The Current Node Data
    def data(self):
        return self.current.data
    
    # Iterate To The Next Node
    def next(self):
        self.current = self.current.next
        return self

    # Return The Current Node
    def current(self):
        return self.current


# LinkedList Class Impelmentation
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.length = 0
    
    # Change The Head Node With The New Node
    def insert_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    # Append New Node At The End Of The LinkedList
    def append_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
    
    # Delete The Head Node
    def delete_head(self):
        if self.head is None:
            return
        self.head = self.head.next
    
    # Insert New Node After Given Node
    def insert_after(self, node, data):
        new_node = Node(data)
        current = self.find_node(node) 
        if current.next is None and current is not None:
            self.append_node(data)
            return
        if current is not None: 
            new_node.next = current.next
            current.next = new_node

    # Delete Given Node By Data
    def delete_node(self, node):
        node_to_delete = self.find_node(node) 

        if node_to_delete is not None:
            parent_node_to_delete = self.find_parent(node) 
            if parent_node_to_delete is not None:
                parent_node_to_delete.next = node_to_delete.next
            else:
                self.delete_head()
    
    # Find Node By Data And Return That Node
    def find_parent(self, data):
        itr = self.begin()
        while itr.current() is not None:
            if itr.current().next == data:
                return itr.current()
        return None
        
    # Find Node By Data And Return That Node
    def find_node(self, data):
        itr = self.begin()
        while itr.current() is not None:
            if itr.data == data:
                return itr.current()
            itr.next()
        return None
    
    # Return the length of the list using an iterator
    def get_length_itr(self):
        count = 0 
        itr = self.begin()
        while itr.current():
            count += 1
            itr.next()
        return count

    # Init Iterator
    def begin(self):
        itr = ListIterator(self.head)
        return itr
