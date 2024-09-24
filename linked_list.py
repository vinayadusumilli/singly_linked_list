from nodes import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def print_data(self):
        n = self.head
        if n is None:
            print("Linked list is Empty")
        else:
            while n is not None:
                print(n.data)
                n = n.ref
                print(n)

    def add_begin_node(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
