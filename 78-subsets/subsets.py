class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def backtrack(arr, i):
            nonlocal res
            if i == len(nums):
                res.append(arr)
                return
            
            backtrack(arr, i+1)
            backtrack(arr + [nums[i]], i+1)
        
        backtrack([], 0)
        
        return res
                
        
        