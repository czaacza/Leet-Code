class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            s_sorted = \\.join(sorted(s))
            if s_sorted not in group:
                group[s_sorted] = []
            group[s_sorted].append(s)
        
        return group.values()

        