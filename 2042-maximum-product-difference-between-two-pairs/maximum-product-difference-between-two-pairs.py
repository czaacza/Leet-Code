class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1, max2 = -math.inf, -math.inf
        min1, min2 = math.inf, math.inf
        
        for n in nums:
            if n > max2:
                if n > max1:
                    max2 = max1
                    max1 = n
                else:
                    max2 = n
            
            if n < min2:
                if n < min1:
                    min2 = min1
                    min1 = n
                else:
                    min2 = n
        
        return (max1 * max2) - (min1 * min2)