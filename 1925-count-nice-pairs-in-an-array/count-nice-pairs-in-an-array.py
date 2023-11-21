class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(s):
            reversed_str = ''
            for i in range(len(s)-1, -1, -1):
                reversed_str += s[i]
            return int(reversed_str)

        rev_values = []
        for i in range(len(nums)):
            rev_values.append(nums[i] - rev(str(nums[i])))

        seen = {}
        res = 0
        for val in rev_values:
            if val not in seen: 
                seen[val] = 1
                continue

            res += seen[val]
            seen[val] += 1

        return res % (10**9 + 7)

            




                





        