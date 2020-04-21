class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def DFS(node: TreeNode, depth: int):
            if node.left == None and node.right == None: return node.val, depth
            if node.left == None: return DFS(node.right, depth + 1)
            if node.right == None: return DFS(node.left, depth + 1)
        
            nl, ll = DFS(node.left, depth + 1)
            nr, lr = DFS(node.right, depth + 1)
            
            if ll > lr: return nl, ll
            if lr > ll: return nr, lr
            return nl + nr, ll
    
        if root: return DFS(root, 0)[0]
        return 0

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(7)
root.right = TreeNode(3)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(8)

print(Solution().deepestLeavesSum(root))