# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def DFS(node, bounds):
            if not node:
                return True
            if not (bounds[0] < node.val < bounds[1]):
                return False

            return DFS(node.left,[bounds[0],node.val]) and DFS(node.right, [node.val, bounds[1]])
                    
        return DFS(root, [-math.inf, math.inf])