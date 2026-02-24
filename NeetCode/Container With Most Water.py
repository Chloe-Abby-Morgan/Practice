class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = -1
        left = 0
        right = len(heights) - 1

        while left < right:
            if (right - left) * min(heights[left], heights[right]) > maxWater:
                maxWater = (right - left) * min(heights[left], heights[right])
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return maxWater

if __name__ == "__main__":
    print(Solution().maxArea([1,7,2,5,4,7,3,6]))