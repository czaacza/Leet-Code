class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        for l in str(bin(n)):
            if l == '1':
                counter += 1
        return counter
        