def max_path_sum(tree_data):
    class tree_node:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    class solution:
        def __init__(self):
            self.max_sum = float('-inf')
        
        def max_path_sum(self, root: tree_node) -> int:
            def max_gain(node):
                if not node:
                    return 0
                
                left_gain = max(max_gain(node.left), 0)
                right_gain = max(max_gain(node.right), 0)
                
                current_sum = node.val + left_gain + right_gain
                self.max_sum = max(self.max_sum, current_sum)
                
                return node.val + max(left_gain, right_gain)
            
            max_gain(root)
            return self.max_sum

    def list_to_tree(lst, idx=0):
        if idx < len(lst) and lst[idx] is not None:
            node = tree_node(lst[idx])
            node.left = list_to_tree(lst, 2 * idx + 1)
            node.right = list_to_tree(lst, 2 * idx + 2)
            return node
        return None

    root = list_to_tree(tree_data)
    solution_instance = solution()
    return solution_instance.max_path_sum(root)