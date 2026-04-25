# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            last = stack.pop()
            if last:
                if self.sameTree(last,subRoot):
                    return True
                stack.append(last.left)
                stack.append(last.right)
        return False

    def sameTree(self,a,b):
        stack = [(a,b)]

        while stack:
            lasta, lastb = stack.pop()

            if (lasta and not lastb) or (not lasta and lastb):
                    return False
            if lasta and lastb:
                if lasta != lastb and lasta.val != lastb.val:
                    return False
                stack.append((lasta.left, lastb.left))
                stack.append((lasta.right, lastb.right))
        return True