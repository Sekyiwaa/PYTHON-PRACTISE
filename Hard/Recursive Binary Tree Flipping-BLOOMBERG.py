def flip_binary_tree(tree_data):
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def list_to_tree(lst, idx=0):
        if idx < len(lst) and lst[idx] is not None:
            node = TreeNode(lst[idx])
            node.left = list_to_tree(lst, 2 * idx + 1)
            node.right = list_to_tree(lst, 2 * idx + 2)
            return node
        return None

    def tree_to_list(node):
        if not node:
            return []
        result = []
        queue = [node]
        while any(queue):
            current = queue.pop(0)
            if current:
                result.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
            else:
                result.append(None)
        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()
        return result

    def flip_tree(root):
        if not root:
            return None

        if not root.left and not root.right:
            return root

        flipped_root = flip_tree(root.left)

        root.left.left = root.right
        root.left.right = root

        root.left = None
        root.right = None

        return flipped_root

    # Convert input list to tree
    root = list_to_tree(tree_data)

    # Flip the tree
    new_root = flip_tree(root)

    # Convert the flipped tree back to list
    return tree_to_list(new_root)