def find_max_nodes_per_level(tree_values):
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def build_tree(values):
        if not values:
            return None
        nodes = [None if val is None else Node(val) for val in values]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    def find_max_nodes(root):
        if root is None:
            return []

        max_nodes = []
        queue = [root]

        while queue:
            level_max = float('-inf')
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.pop(0)
                level_max = max(level_max, node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            max_nodes.append(level_max)

        return max_nodes

    root = build_tree(tree_values)
    return find_max_nodes(root)