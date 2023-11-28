class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        max_freq = 0
        max_num = 0
        
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            if freq[nums[i]] > max_freq:
                max_freq = freq[nums[i]]
                max_num = nums[i]
                
        return max_num
        
            
                
        
        