class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 0

        for i in range(len(nums)-1, -1, -1):
            curr_max = 0
            for j in range(i, len(nums)):
                if nums[j] <= nums[i]:
                    continue
                curr_max = max(curr_max, dp[j])
            dp[i] = curr_max + 1
            res = max(res, dp[i])

        return res
                
            




        