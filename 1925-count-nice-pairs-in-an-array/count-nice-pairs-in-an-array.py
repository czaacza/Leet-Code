class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(s):
            reversed_str = ''
            for i in range(len(s)-1, -1, -1):
                reversed_str += s[i]
            return int(reversed_str)

        rev_values = {}
        for i in range(len(nums)):
            minus = nums[i] - rev(str(nums[i]))

            if minus not in rev_values:
                rev_values[minus] = []

            rev_values[minus].append(i)

        res = 0
        seen = {}
        for arr in rev_values.values():
            res += len(arr) * (len(arr) - 1) // 2

        return res % (10**9 + 7)



                





        