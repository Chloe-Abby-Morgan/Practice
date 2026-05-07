class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in nums:
                if i in path:
                    continue
                else:
                    path.append(i)
                    backtrack(path)
                    path.pop()
            
        backtrack([])
        return res