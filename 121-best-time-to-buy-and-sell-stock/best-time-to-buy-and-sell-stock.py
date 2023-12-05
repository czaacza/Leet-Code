class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        max_price = 0
        while r <= len(prices)-1:
            if prices[r] < prices[l]:
                l = r
                continue
            max_price = max(max_price, prices[r] - prices[l])
            r += 1
        return max_price
            
            