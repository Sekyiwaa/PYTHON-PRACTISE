def create_stack(input_data):
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class Stack:
        def __init__(self):
            self.head = None

        def is_empty(self):
            return self.head is None

        def push(self, data):
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

        def pop(self):
            if self.is_empty():
                return None
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data

        def peek(self):
            if self.is_empty():
                return None
            return self.head.data

        def process_operations(self, values, operations):
            output = []
            value_index = 0
            for operation in operations:
                if operation == "push" and value_index < len(values):
                    self.push(values[value_index])
                    value_index += 1
                elif operation == "pop":
                    result = self.pop()
                    if result is not None:
                        output.append(result)
                elif operation == "peek":
                    result = self.peek()
                    if result is not None:
                        output.append(result)
            return output

    values = input_data.get('values', [])
    operations = input_data.get('operations', [])
    
    stack_instance = Stack()
    return stack_instance.process_operations(values, operations)