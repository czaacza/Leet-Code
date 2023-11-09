class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = i
        
        for i in range(len(nums)):
            to_find = target - nums[i]
            if to_find in seen and seen[to_find] != i :
                return [i, seen[to_find]]