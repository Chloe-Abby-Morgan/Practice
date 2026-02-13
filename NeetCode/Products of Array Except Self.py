class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixSum = [0] * len(nums)
        suffixSum = [0] * len(nums)
        prefixSum[0] = 1
        suffixSum[-1] = 1
    
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            suffixSum[i] = suffixSum[i+1] * nums[i+1]

        return [prefixSum[i] * suffixSum[i] for i in range(len(nums))]
    
if __name__ == "__main__":
    lst = [1,2,4,6]
    print(Solution().productExceptSelf(lst))