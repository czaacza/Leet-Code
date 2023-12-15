class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(arr):
            if len(arr) == len(nums):
                res.append(arr)
                return 
            
            for j in range(len(nums)):
                if nums[j] in arr:
                    continue
                    
                backtrack(arr + [nums[j]])
        
        backtrack([])
        return res
        