class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        rate = right

        while left <= right:
            mid = (left + right) // 2
            total = 0
        
            for i in piles:
                total += math.ceil(i/mid)
            
            if total <= h:
                right = mid - 1
                rate = mid
            else:
                left = mid + 1
        return rate
