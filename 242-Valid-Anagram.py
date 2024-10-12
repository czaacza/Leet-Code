class Solution:        
    def isAnagram(self, s: str, t: str) -> bool:
        def build_counter(s):
            counter = {}
            for letter in s:
                if not (letter in counter):
                    counter[letter] = 0  
                counter[letter] += 1
            return counter

        counter_s = build_counter(s)
        counter_t = build_counter(t)

        for key in set(list(counter_s.keys()) + list(counter_t.keys())):
            if (key not in counter_s or key not in counter_t) or counter_s[key] != counter_t[key]:
                return False
        
        return True