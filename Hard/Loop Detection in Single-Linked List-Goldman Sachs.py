def has_loop_solution(input_data):
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def has_loop(head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    def list_to_linked_list(lst, pos):
        head = None
        tail = None
        nodes = []

        for index, value in enumerate(lst):
            new_node = Node(value)
            nodes.append(new_node)
            if not head:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node

        # Create a loop if pos is not -1
        if pos != -1 and nodes:
            tail.next = nodes[pos]

        return head

    # Extract list_data and pos from the input_data dictionary
    list = input_data['list']
    pos = input_data['pos']

    linked_list_head = list_to_linked_list(list, pos)
    return has_loop(linked_list_head)