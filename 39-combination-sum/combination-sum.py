class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(arr, i):
            nonlocal res
            curr_sum = sum(arr)
            if i == len(candidates):
                return
            if curr_sum == target:
                res.append(arr)
                return
            elif curr_sum > target:
                return
            
            for i in range(i, len(candidates)):
                backtrack(arr + [candidates[i]], i)
                
        backtrack([], 0)
        return res
                
                    
        