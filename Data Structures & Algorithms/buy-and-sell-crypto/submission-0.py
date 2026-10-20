class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, forward = 0, 0

        max_profit = 0
        while forward != len(prices):
            max_profit = max(max_profit, prices[forward] - prices[left])
            if prices[forward] < prices[left]:
                left = forward
            forward += 1
        return max_profit