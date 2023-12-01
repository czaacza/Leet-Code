class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        str1, str2 = "", ""
        for word in word1:
            for l in word:
                str1 += l
        for word in word2:
            for l in word:
                str2 += l
        if str1 == str2:
            return True
        return False
                
        