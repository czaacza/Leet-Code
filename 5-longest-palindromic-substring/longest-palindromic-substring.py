class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len_p = ''
        for i in range(len(s)):
#           when palindrome is of odd length
            l, r = i, i
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                if r - l + 1 > len(max_len_p):
                        max_len_p = s[l: r+1]
                l -= 1
                r += 1
                
#           when palindrome is of even length
            l, r = i, i+1
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                if r - l + 1 > len(max_len_p):
                    max_len_p = s[l: r+1] 
                l -= 1
                r += 1
                               
        
        return max_len_p
            
        