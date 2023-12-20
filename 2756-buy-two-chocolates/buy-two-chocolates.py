class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1, min2 = math.inf, math.inf
        for p in prices:
            if p < min2:
                if p < min1:
                    min2 = min1
                    min1 = p
                else:
                    min2 = p
        
        moneyLeft = money - (min1 + min2)
        
        return moneyLeft if moneyLeft >= 0 else money
                    