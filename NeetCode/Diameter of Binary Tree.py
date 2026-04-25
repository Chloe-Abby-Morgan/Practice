# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        maxPath = 0
        
        while stack:
            last = stack.pop()
            if last:
                maxPath = max(maxPath,self.maxDepth(last.left) + self.maxDepth(last.right))
                stack.append(last.left)
                stack.append(last.right)
        return maxPath

    def maxDepth(self, r):
        stack = [[r,1]]
        depth = 0

        if not r:
            return 0
        
        while stack:
            last, d = stack.pop()
            if last:
                depth = max(depth, d)
                stack.append([last.left, d+1])
                stack.append([last.right, d+1])
        return depth