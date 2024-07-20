import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    # ... existing test cases ...

    def test_count_list(self):
        ll = LinkedList()
        self.assertEqual(ll.count_list(), 0)

        ll.insert_node(1)
        self.assertEqual(ll.count_list(), 1)

        ll.insert_node(2)
        ll.insert_node(3)
        self.assertEqual(ll.count_list(), 3)

    def test_insert_head(self):
        ll = LinkedList()
        ll.insert_head(1)
        self.assertEqual(ll.head.data, 1)

        ll.insert_head(2)
        self.assertEqual(ll.head.data, 2)
        self.assertEqual(ll.head.next.data, 1)

    def test_insert_after(self):
        ll = LinkedList()
        ll.insert_node(1)
        ll.insert_node(2)
        ll.insert_node(3)

        ll.insert_after(2, 4)
        node, _ = ll.find_node_data(4)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 4)

        ll.insert_after(3, 5)
        node, _ = ll.find_node_data(5)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 5)

    def test_delete_head(self):
        ll = LinkedList()
        ll.insert_node(1)
        ll.insert_node(2)
        ll.insert_node(3)

        ll.delete_head()
        self.assertEqual(ll.head.data, 2)

        ll.delete_head()
        self.assertEqual(ll.head.data, 3)

    def test_delete_node(self):
        ll = LinkedList()
        ll.insert_node(1)
        ll.insert_node(2)
        ll.insert_node(3)

        ll.delete_node(2)
        node, _ = ll.find_node_data(2)
        self.assertIsNone(node)

        ll.delete_node(3)
        node, _ = ll.find_node_data(3)
        self.assertIsNone(node)

if __name__ == "__main__":
    unittest.main()