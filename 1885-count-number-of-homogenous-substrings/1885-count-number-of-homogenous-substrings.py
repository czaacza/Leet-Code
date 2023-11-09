class Solution:
    def countHomogenous(self, s: str) -> int:
        l, r, total = 0, 0, 0

        while r < len(s):
            total += 1
            if s[l] == s[r]:
                total += r-l
            else:
                while(l != r):
                    l += 1
            r += 1
        
        return total % (10**9 + 7)
        