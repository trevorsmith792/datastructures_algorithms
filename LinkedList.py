class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # The list starts as empty

    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:
            self.head = new_node  # If the list is empty, new node becomes the head
            return
        last_node = self.head
        while last_node.next:  # Traverse until the last node
            last_node = last_node.next
        last_node.next = new_node  # Point the last node's next to the new node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Indicating the end of the list

# Example usage
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

linked_list.display()  # Output: 10 -> 20 -> 30 -> None
