class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        a_vowels = 0
        b_vowels = 0

        for i in range(len(s) // 2):
            if s[i] in vowels:
                a_vowels += 1
            if s[-1-i] in vowels:
                b_vowels += 1
        
        return a_vowels == b_vowels




        