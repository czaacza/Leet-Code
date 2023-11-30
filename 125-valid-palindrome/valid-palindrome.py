class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for l in s.lower():
            print('l', ord(l))
            if ord(l) >= 97 and ord(l) <= 122 or ord(l) >= 48 and ord(l) <= 57:
                res += l
        for i in range(len(res)):
            if res[i] != res[-1-i]:
                return False
        return True
            
            
            
            
        