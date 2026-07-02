class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def pre_order_dfs(node, result=None):
    if result is None:
        result = []
        
    if node:
        result.append(node.val)              # Visit the root
        pre_order_dfs(node.left, result)     # Traverse left
        pre_order_dfs(node.right, result)    # Traverse right
        
    return result


def in_order_dfs(node, result=None):
    if result is None:
        result = []
        
    if node:
        in_order_dfs(node.left, result)      # Traverse left
        result.append(node.val)              # Visit the root
        in_order_dfs(node.right, result)     # Traverse right
        
    return result


def post_order_dfs(node, result=None):
    if result is None:
        result = []
        
    if node:
        post_order_dfs(node.left, result)    # Traverse left
        post_order_dfs(node.right, result)   # Traverse right
        result.append(node.val)              # Visit the root
        
    return result


def post_order_dfs(node, result=None):
    if result is None:
        result = []
        
    if node:
        post_order_dfs(node.left, result)    # Traverse left
        post_order_dfs(node.right, result)   # Traverse right
        result.append(node.val)              # Visit the root
        
    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Run the traversals
print("Pre-order: ", pre_order_dfs(root))
print("In-order:  ", in_order_dfs(root))
print("Post-order:", post_order_dfs(root))
