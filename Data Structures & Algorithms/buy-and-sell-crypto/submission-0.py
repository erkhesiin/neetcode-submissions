class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = prices[0]

        for sell in prices:
            profit = max(profit, sell - minimum)
            minimum = min(minimum, sell)
        return profit