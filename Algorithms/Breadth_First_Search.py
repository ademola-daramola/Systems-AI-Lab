from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def breadth_first_search(root):
    # If the tree is empty, return an empty list
    if not root:
        return []
        
    result = []
    # Initialize the queue with the root node
    queue = deque([root])
    
    while queue:
        # Dequeue the first node in the queue
        current_node = queue.popleft()
        
        # Process the current node
        result.append(current_node.val)
        
        # Enqueue the left child if it exists
        if current_node.left:
            queue.append(current_node.left)
            
        # Enqueue the right child if it exists
        if current_node.right:
            queue.append(current_node.right)
            
    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Run the traversal
print("Breadth-First Search (Level-order):", breadth_first_search(root))