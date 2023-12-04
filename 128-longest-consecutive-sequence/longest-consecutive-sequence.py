class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_conv = 0
        seen = set(nums)

        for n in nums:
            curr_conv = 1

            if n -1 in seen:
                continue

            while n + curr_conv in seen:
                curr_conv += 1

            max_conv = max(max_conv, curr_conv)
            
        return max_conv