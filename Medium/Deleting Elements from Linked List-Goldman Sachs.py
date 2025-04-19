def linked_list_operations(elements):
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None
    class LinkedList:
        def __init__(self):
            self.head = None
        def append(self, data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
        def delete_first_and_second_elements(self):
            if self.head is None:
                return
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next.next
        def display(self):
            result = []
            current = self.head
            while current:
                result.append(current.data)
                current = current.next
            return result
    ll = LinkedList()
    for elem in elements:
        ll.append(elem)
    ll.delete_first_and_second_elements()
    return ll.display()