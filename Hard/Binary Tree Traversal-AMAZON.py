def zigzag_level_order_solution(tree_data):
    class tree_node:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def list_to_tree(lst, idx=0):
        if idx < len(lst) and lst[idx] is not None:
            node = tree_node(lst[idx])
            node.left = list_to_tree(lst, 2 * idx + 1)
            node.right = list_to_tree(lst, 2 * idx + 2)
            return node
        return None

    def zigzag_level_order(root):
        if not root:
            return []
        
        result = []
        queue = [root]
        level = 0
        
        while queue:
            level_values = []
            size = len(queue)
            
            for _ in range(size):
                node = queue.pop(0)
                level_values.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level % 2 == 1:
                level_values.reverse()
            
            result.append(level_values)
            level += 1
        
        return result

    root = list_to_tree(tree_data)
    return zigzag_level_order(root)