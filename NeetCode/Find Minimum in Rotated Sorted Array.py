class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right, output = 0, len(nums) - 1, nums[0]
        
        while left <= right:
            if nums[left] < nums[right]:
                output = min(output, nums[left])
                break

            mid = left + (right - left) // 2
            output = min(output, nums[mid])

            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return output