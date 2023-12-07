class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seen = set()
        max_len = 0
        
        while r <= len(s)-1:
            curr_letter = s[r]
            while curr_letter in seen:
                seen.remove(s[l])
                l += 1
            r += 1
            seen.add(curr_letter)
            max_len = max(max_len, r - l)
        
        return max_len
            

        

        