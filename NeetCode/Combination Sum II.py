class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(total, step, path):
            if total == target:
                res.append(path[:])
                return
            if total > target or step == len(candidates):
                return

            path.append(candidates[step])
            backtrack(total+candidates[step],step+1,path)

            path.pop()

            while step+1 < len(candidates) and candidates[step] == candidates[step+1]:
                step += 1
            backtrack(total,step+1,path)
        
        backtrack(0,0,[])
        return res