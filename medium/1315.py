from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]

def sumEvenGrandparent(root: TreeNode) -> int:
    def BFS(root):
        visited = []
        if root:
            visited.append(root)
        current = root
        while current :
            if current.left:
                visited.append(current.left)
            if current.right:
                visited.append(current.right)
            visited.pop(0)
            if not visited:
                break
            current = visited[0]
    sum = 0
    for i in range(len(BFS(root))):
        if root[i] is not None and root[i]%2 == 0:
            if (4*i) + 3 < len(root) and root[(4*i) + 3] is not None: sum += root[(4*i) + 3]
            if (4*i) + 4 < len(root) and root[(4*i) + 4] is not None: sum += root[(4*i) + 4]  
            if (4*i) + 5 < len(root) and root[(4*i) + 5] is not None: sum += root[(4*i) + 5]  
            if (4*i) + 6 < len(root) and root[(4*i) + 6] is not None: sum += root[(4*i) + 6]  
    return sum
        
print(sumEvenGrandparent(root))