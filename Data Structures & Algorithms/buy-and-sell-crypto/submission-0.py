class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        max_profit_so_far = 0
        for price in prices:
            max_profit_so_far = max(max_profit_so_far, price-min_so_far)
            min_so_far = min(min_so_far, price)
        
        return max_profit_so_far