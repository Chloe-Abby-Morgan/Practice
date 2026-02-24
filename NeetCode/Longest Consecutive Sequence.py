class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        length = -1
        longest = -1
        
        for i in set(nums):
            if i-1 not in set(nums):
                length = 1
                
                while i + length in set(nums):
                    length += 1
                longest = max(length, longest)
        return longest

if __name__ == "__main__":
    print(Solution().longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]))