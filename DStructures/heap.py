class Heap:
    def __init__(self) -> None:
        self.dataList = []
        self.size = 0

    def insert_node(self, data):
        i = self.size
        self.dataList[i] = data
        self.size += 1

        parent_index = (i - 1) // 2

        while i != 0 and self.dataList[i] < self.dataList[parent_index]:
            self.dataList[i], self.dataList[parent_index] = self.dataList[parent_index], data 
            i = parent_index

            parent_index = (i - 1) // 2

    
    def get_size(self):
        return self.size
    
    def print_list(self):
        print_data = "" 
        for i in self.dataList:
            print_data += i + " - " 
        print(print_data)


heap = Heap()

# Test inserting nodes
heap.insert_node(5)
heap.insert_node(3)
heap.insert_node(8)
heap.insert_node(1)
heap.insert_node(10)

# Test get_size method
assert heap.get_size() == 5

# Test print_list method
heap.print_list()  