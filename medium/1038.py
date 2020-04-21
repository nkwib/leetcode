# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        mappedTree = []
        def BFS(node):
            mappedTree.append(node.val)
            if node.left: BFS(node.left)
            if node.right: BFS(node.right)
        BFS(root)
        return mappedTree
Input = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
Output = [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]
root = TreeNode(4)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

#print(Solution().bstToGst(root))

Inp = filter(lambda e: isinstance(e, int), Input)
for i in Input:
    if i != None:
        

