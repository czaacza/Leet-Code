class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        
        for i in range(len(dp)-2, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(dp)-1 and s[i: i + len(word)] in wordDict and dp[i + len(word)] == True:
                    dp[i] = True
        
        return dp[0]
            
            
                    
                
        