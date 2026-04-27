# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        output = []
        level = 0
        q = [root]
        
        while q:
            output.append([])
            for i in range(len(q)):
                first = q.pop(0)
                if first:
                    output[level].append(first.val)
                    q.append(first.left)
                    q.append(first.right)
                
            level += 1
        return output[:-1]