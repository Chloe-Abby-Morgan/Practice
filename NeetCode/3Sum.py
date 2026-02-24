class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pairs = []
        nums.sort()

        for i in range(len(nums)):
            left = i+1
            right = len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0 and [nums[i], nums[left], nums[right]] not in pairs:
                    pairs.append([nums[i], nums[left], nums[right]])
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return pairs

if __name__ == "__main__":
    print(Solution().threeSum([-1,0,1,2,-1,-4]))