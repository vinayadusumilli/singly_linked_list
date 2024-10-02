from linked_list import LinkedList


def get_preference(message) -> int:
    """
    Takes a message to display, gets user input, and returns user input as an integer.
    :param message: The message to display to the user.
    :return: The user input as an integer.
    """
    while True:
        try:
            return int(input(message))
        except ValueError as e:
            print(f"Not a valid input, Reason: {e}")


def get_preference_data(message) -> str:
    """
    Takes a message to display, gets user input, and returns it as a string.
    :param message: The message to display to the user.
    :return: The user input as a string.
    """
    return input(message)


create = True
while create:
    limit: int = get_preference(message="Linked List Memory\nSize of Singly Linked List: ")
    singly_linked = LinkedList(limit)
    print(f"Linked List created with a size of {limit}")
    is_on = True
    while is_on:
        choice: int = get_preference(message="1. Add New Node at the Beginning of Linked List\n"
                                             "2. Add New Node to the End of Linked List\n"
                                             "3. Add New Node After a Node\n"
                                             "4. Add New Node Before a Node\n"
                                             "5. Delete Beginning Node\n"
                                             "6. Delete End Node\n"
                                             "7. Delete Node After a Node\n"
                                             "8. Delete Node Before a Node\n"
                                             "9. Display Linked List\n"
                                             "10. Initialize a New Linked List\n"
                                             "11. Quit\n"
                                             "Choose an operation on your linked list: ")
        if choice == 1:
            new_node = get_preference_data(message="Enter data for the new node at the beginning: ")
            singly_linked.add_begin_node(new_node)
        elif choice == 2:
            new_node = get_preference_data(message="Enter data for the new node at the end: ")
            singly_linked.add_end_node(new_node)
        elif choice == 3:
            new_node = get_preference_data(message="Enter data for the new node: ")
            existing_after_node_data = get_preference_data(message="Enter the data of the node to add after: ")
            singly_linked.add_after_node(data=new_node, x=existing_after_node_data)
        elif choice == 4:
            new_node = get_preference_data(message="Enter data for the new node: ")
            existing_before_node_data = get_preference_data(message="Enter the data of the node to add before: ")
            singly_linked.add_before_node(data=new_node, y=existing_before_node_data)
        elif choice == 5:
            singly_linked.remove_begin_node()
        elif choice == 6:
            singly_linked.remove_end_node()
        elif choice == 7:
            existing_after_node_remove = get_preference_data(
                message="Enter the data of the node to delete after: ")
            singly_linked.remove_after_node(x=existing_after_node_remove)
        elif choice == 8:
            existing_before_node_remove = get_preference_data(
                message="Enter the data of the node to delete before: ")
            singly_linked.remove_before_node(y=existing_before_node_remove)
        elif choice == 9:
            singly_linked.display()
        elif choice == 10:
            confirm = get_preference(message=f"1. Confirm\n"
                                             f"2. Cancel\n"
                                             f"Are you sure you want to clear the linked list and create a new one? ")
            if confirm == 1:
                is_on = False  # Ends the current linked list session
        elif choice == 11:
            create = False  # Ends the entire program
            break
        else:
            print("Invalid choice! Please try again.")
