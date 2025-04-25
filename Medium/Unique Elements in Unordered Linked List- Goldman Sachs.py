def remove_duplicates_from_linked_list(input_list):
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def create_linked_list(values):
        if not values:
            return None
        head = Node(values[0])
        current = head
        for value in values[1:]:
            current.next = Node(value)
            current = current.next
        return head

    def linked_list_to_list(head):
        result = []
        current = head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def remove_duplicates(head):
        if head is None:
            return head

        current = head
        seen = set([current.data])

        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next

        return head

    head = create_linked_list(input_list)
    head = remove_duplicates(head)
    return linked_list_to_list(head)