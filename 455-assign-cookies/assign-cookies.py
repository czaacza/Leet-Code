class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        g_i = 0
        s_i = 0
        res = 0
        while s_i <= len(s) - 1 and g_i <= len(g) - 1:
            while s_i <= len(s)-1 and s[s_i] < g[g_i]:
                s_i += 1
            if s_i > len(s) - 1:
                return res
            res += 1
            s_i += 1
            g_i += 1
        return res
            