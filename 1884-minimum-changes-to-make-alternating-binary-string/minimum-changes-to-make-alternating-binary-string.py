class Solution:
    def minOperations(self, s: str) -> int:      
        counter1, counter2 = 0, 0
        for i in range(len(s)):
            if i % 2 == 0 and s[i] != '1' or i % 2 == 1 and s[i] != '0':
                counter1 += 1
        
        for i in range(len(s)):
            if i % 2 == 0 and s[i] != '0' or i % 2 == 1 and s[i] != '1':
                counter2 += 1
        
        return min(counter1, counter2)
            
        