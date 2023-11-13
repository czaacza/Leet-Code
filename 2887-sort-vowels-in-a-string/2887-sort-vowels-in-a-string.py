class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        idx_to_change = set()
        letters_to_change = []
        t = [-1] * len(s)

        for i in range(len(s)):
            if s[i] in vowels:
                idx_to_change.add(i)
                letters_to_change.append(s[i])
            t[i] = s[i]

        letters_to_change.sort()    

        letter_count = 0
        for i in range(len(s)):
            if i in idx_to_change:
                t[i] = letters_to_change[letter_count]
                letter_count += 1
        
        return ''.join(t)


        