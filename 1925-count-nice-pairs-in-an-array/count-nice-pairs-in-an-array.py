class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            result = 0
            while num:
                result = result * 10 + num % 10
                num //= 10
            
            return result

        rev_values = []
        for i in range(len(nums)):
            rev_values.append(nums[i] - rev(nums[i]))

        seen = {}
        res = 0
        for val in rev_values:
            if val not in seen: 
                seen[val] = 1
                continue

            res += seen[val]
            seen[val] += 1

        return res % (10**9 + 7)       