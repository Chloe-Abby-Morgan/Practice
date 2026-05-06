class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(step,path):
            if step == len(nums):
                result.append(path[:])
                return

            path.append(nums[step])
            backtrack(step+1,path)
            
            path.pop()
            backtrack(step+1,path)

        backtrack(0,[])
        return result