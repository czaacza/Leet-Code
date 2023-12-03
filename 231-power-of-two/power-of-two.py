class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        counter = 0
        for l in bin(n):
            if l == '1':
                counter += 1
            if counter > 1:
                return False
        return True
        