# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root,1]]
        maxDepth = 0

        if not root:
            return 0

        while stack:
            last, depth = stack.pop()
            if last:
                maxDepth = max(maxDepth, depth)
                stack.append([last.left,depth+1])
                stack.append([last.right,depth+1])
        return maxDepth