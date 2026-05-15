class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        profit, low, i = 0, prices[0], 1
        while i < len(prices):
            profit = max(profit, prices[i] - low)
            low = min(low, prices[i])
            i += 1
        return profit