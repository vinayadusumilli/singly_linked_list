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

    def add_begin_node(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end_node(self, data):
        new_node = Node(data)
        n = self.head
        if n is None:
            new_node.ref = new_node
            self.head = new_node
        else:
            before_node = None
            while n is not None:
                before_node = n
                n = n.ref
            before_node.ref = new_node

    def add_between_nodes(self, data, node_data):
        global current_ref, next_ref
        new_node = Node(data)
        n = self.head
        if n is None:
            new_node.ref = self.head
            self.head = new_node
        else:
            current_ref = None
            next_ref = None
            while n is not None:
                current_ref = n
                next_ref = n.ref
                if n.data == node_data:
                    break
                else:
                    n = n.ref
        current_ref.ref = new_node
        next_ref.ref = new_node


