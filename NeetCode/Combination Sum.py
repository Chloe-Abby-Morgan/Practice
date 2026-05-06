class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(step,total, path):
            if total == target:
                res.append(path[:])
                return
            elif step >= len(nums) or total > target:
                return
            
            path.append(nums[step])
            backtrack(step,total+nums[step],path)

            path.pop()
            backtrack(step+1,total,path)
                
        backtrack(0,0,[])
        return res