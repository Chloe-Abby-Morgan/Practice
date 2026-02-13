class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elts = {}

        for index, num in enumerate(nums):
            elts[num] = index
        
        for index, elt in enumerate(nums):
            difference = target - elt
            if difference in elts and elts[difference] != index:
                return [index, elts[difference]]
        return []

if __name__ == "__main__":
    lst = [3,4,5,6]
    target = 7
    print(Solution().twoSum(lst, target))