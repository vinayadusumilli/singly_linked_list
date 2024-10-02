from nodes import Node


class LinkedList:
    def __init__(self, size):
        self.size = size  # The maximum number of nodes allowed
        self.count = 0  # The current number of nodes
        self.head = None  # The head node of the list

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" -> " if n.ref else "\n")
                n = n.ref

    def add_begin_node(self, data):
        if self.count >= self.size:
            print("Linked list is full")
        else:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            self.count += 1
            print(f"Node with data '{data}' added at the beginning.")

    def add_end_node(self, data):
        if self.count >= self.size:
            print("Linked list is full")
        else:
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                n = self.head
                while n.ref is not None:
                    n = n.ref
                n.ref = new_node
            self.count += 1
            print(f"Node with data '{data}' added at the end.")

    def add_after_node(self, data, x):
        if self.count >= self.size:
            print("Linked list is full!")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.ref
            if n is None:
                print(f"Node with data '{x}' not found.")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node
                self.count += 1
                print(f"Node with data '{data}' added after '{x}'.")

    def add_before_node(self, data, y):
        if self.count >= self.size:
            print("Linked list is full!")
        else:
            if self.head is None:
                print("Linked list is empty.")
                return

            if self.head.data == y:  # Special case: Add before head
                self.add_begin_node(data)
                return

            n = self.head
            while n.ref is not None and n.ref.data != y:
                n = n.ref

            if n.ref is None:
                print(f"Node with data '{y}' not found.")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node
                self.count += 1
                print(f"Node with data '{data}' added before '{y}'.")

    def remove_begin_node(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            print(f"Node with data '{self.head.data}' removed from the beginning.")
            self.head = self.head.ref
            self.count -= 1

    def remove_end_node(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            if self.head.ref is None:  # Only one node in the list
                print(f"Node with data '{self.head.data}' removed from the end.")
                self.head = None
            else:
                n = self.head
                while n.ref.ref is not None:
                    n = n.ref
                print(f"Node with data '{n.ref.data}' removed from the end.")
                n.ref = None
            self.count -= 1

    def remove_after_node(self, x):
        n = self.head
        while n is not None and n.data != x:
            n = n.ref
        if n is None or n.ref is None:
            print(f"No node found after node with data '{x}'.")
        else:
            print(f"Node with data '{n.ref.data}' removed after '{x}'.")
            n.ref = n.ref.ref
            self.count -= 1

    def remove_before_node(self, y):
        if self.head is None or self.head.ref is None:
            print("No nodes to remove before.")
        elif self.head.ref.data == y:  # Special case: Remove before second node (head)
            print(f"Node with data '{self.head.data}' removed before '{y}'.")
            self.head = self.head.ref
            self.count -= 1
        else:
            n = self.head
            while n.ref.ref is not None and n.ref.ref.data != y:
                n = n.ref
            if n.ref is None or n.ref.ref is None:
                print(f"No node found before node with data '{y}'.")
            else:
                print(f"Node with data '{n.ref.data}' removed before '{y}'.")
                n.ref = n.ref.ref
                self.count -= 1
