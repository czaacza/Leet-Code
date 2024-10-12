class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub = {}
        for i in range(len(nums)):
            if (target - nums[i]) in sub:
                return [i, sub[target - nums[i]]]
            sub[nums[i]] = i 
