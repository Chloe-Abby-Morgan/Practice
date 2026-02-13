class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        else:
            return False

if __name__ == "__main__":
    lst = [1,1,2,3,4]
    print(Solution().hasDuplicate(lst))