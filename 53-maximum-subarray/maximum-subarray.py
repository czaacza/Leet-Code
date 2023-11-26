class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, 0
        max_sum = nums[0]
        curr_sum = 0
        while r < len(nums):
            curr_sum += nums[r]
            if curr_sum < 0:
                l = r+1
                r += 1
                max_sum = max(max_sum, curr_sum)
                curr_sum = 0
                continue
            
            max_sum = max(max_sum, curr_sum)
            r += 1
            
        return max_sum
            
        