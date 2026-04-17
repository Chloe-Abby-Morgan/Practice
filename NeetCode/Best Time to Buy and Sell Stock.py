class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        profit = 0

        for i in prices:
            profit = max(profit, i - minBuy)
            minBuy = min(minBuy, i)
        return profit
