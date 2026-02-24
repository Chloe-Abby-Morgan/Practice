class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        prefix = [0] * len(height)
        suffix = [0] * len(height)

        prefix[0] = height[0]
        suffix[-1] = height[-1]

        for i in range(1,len(height)):
            prefix[i] = max(prefix[i-1], height[i])

        for i in range(len(height)-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])

        for i in range(len(height)):
            water += min(prefix[i], suffix[i]) - height[i]

        return water

if __name__ == "__main__":
    print(Solution().trap([0,2,0,3,1,0,1,3,2,1]))