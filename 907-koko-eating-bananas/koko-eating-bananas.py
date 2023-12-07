class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # max = max(piles)
        # min = 1
        r = max(piles)
        l = 1
        min_k = r
        
        while l <= r:
            k = (l + r) // 2
            hours = h
            i = 0
            
            while i <= len(piles) - 1:
                hours -= math.ceil(piles[i] / k)
                i += 1
            
            print('k', k)
            print('i, hours', i, hours)
            if hours >= 0:
                # there are hours left -> too much or ideal
                print('too much')
                r = k - 1
                min_k = min(min_k, k)
            else:
                # not enough hours
                print('too few')
                l = k + 1           
                
        return min_k
                
            
                
                
                
        
        