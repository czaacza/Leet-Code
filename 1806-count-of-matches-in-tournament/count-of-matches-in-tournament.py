class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        def res(n, count):
            if n == 1:
                return count
            
            if n % 2 == 0:
                return res(n / 2,  count + n / 2)
            else:
                return res((n - 1) / 2 + 1, count + (n - 1) / 2)
        
        return int(res(n, 0))
                
                
        