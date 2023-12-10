class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def print_linked_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def merge_sorted_lists(self, other_list):
        dummy = Node()  # No data argument needed
        current = dummy

        current_list1 = self.head
        current_list2 = other_list.head

        while current_list1 is not None and current_list2 is not None:
            if current_list1.data < current_list2.data:
                current.next = Node(current_list1.data)
                current_list1 = current_list1.next
            else:
                current.next = Node(current_list2.data)
                current_list2 = current_list2.next

            current = current.next

        if current_list1 is not None:
            current.next = current_list1
        elif current_list2 is not None:
            current.next = current_list2

        new_list = LinkedList()
        new_list.head = dummy.next

        # Update the tail of the merged list
        while current.next is not None:
            current = current.next
        new_list.tail = current

        return new_list


# Example usage
list1 = LinkedList()
list2 = LinkedList()

list1.insert_at_end(1)
list1.insert_at_end(2)
list1.insert_at_end(4)

list2.insert_at_end(1)
list2.insert_at_end(3)
list2.insert_at_end(4)

print("List 1:")
list1.print_linked_list()

print("\nList 2:")
list2.print_linked_list()

merged_list = list1.merge_sorted_lists(list2)
print("\nMerged List:")
merged_list.print_linked_list()
