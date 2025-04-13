def create_deque(input_data):
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    class Deque:
        def __init__(self):
            self.head = None
            self.tail = None

        def is_empty(self):
            return self.head is None

        def add_front(self, data):
            new_node = Node(data)
            if self.is_empty():
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node

        def add_rear(self, data):
            new_node = Node(data)
            if self.is_empty():
                self.head = new_node
                self.tail = new_node
            else:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node

        def remove_front(self):
            if self.is_empty():
                return None
            data = self.head.data
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return data

        def remove_rear(self):
            if self.is_empty():
                return None
            data = self.tail.data
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            return data

    # Extract values and operations from the input_data dictionary
    values = input_data['values']
    operations = input_data['operations']

    deque_instance = Deque()
    output = []
    value_index = 0

    for operation in operations:
        if operation == "add_front" and value_index < len(values):
            deque_instance.add_front(values[value_index])
            value_index += 1
        elif operation == "add_rear" and value_index < len(values):
            deque_instance.add_rear(values[value_index])
            value_index += 1
        elif operation == "remove_front":
            result = deque_instance.remove_front()
            if result is not None:
                output.append(result)
        elif operation == "remove_rear":
            result = deque_instance.remove_rear()
            if result is not None:
                output.append(result)

    return output