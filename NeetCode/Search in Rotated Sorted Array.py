class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right-left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        def binarySearch(l,r):
            while l <= r:
                mid = l + (r-l) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        result = binarySearch(0, pivot-1)

        if result != -1:
            return result
        else:
            return binarySearch(pivot, len(nums)-1)
            