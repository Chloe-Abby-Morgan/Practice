# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        
        while stack:
            last = stack.pop()
            if last:
                last.left, last.right = last.right, last.left
                stack.append(last.left)
                stack.append(last.right)
        return root
