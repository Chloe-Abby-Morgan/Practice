# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]

        while stack:
            last, lastq = stack.pop()

            if (last and not lastq) or (not last and lastq):
                return False

            if last and lastq:
                if last != lastq and last.val != lastq.val:
                    return False
                stack.append((last.left, lastq.left))
                stack.append((last.right, lastq.right))
        
        return True
