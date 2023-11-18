class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_freq = 1

        l, r = 0, 0
        pre_sum = [nums[0]]
        for i in range(1, len(nums)):
            pre_sum.append(pre_sum[i-1] + nums[i])
            
        while r <= len(nums) - 1:
            target = nums[r]
            window_size = r - l + 1
            final_sum = window_size * target
            if l == 0:
                init_sum = pre_sum[r]
            else:
                init_sum = pre_sum[r] - pre_sum[l-1]
            num_of_operations = final_sum - init_sum
            if num_of_operations > k:
                l += 1
            else:
                max_freq = max(max_freq, window_size)
            r += 1
        
        return max_freq

                

        