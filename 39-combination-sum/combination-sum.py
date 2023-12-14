class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(arr):
            nonlocal res
            curr_sum = sum(candidates[i] for i in arr)
            if curr_sum == target:
                res.append(arr)
                return
            elif curr_sum > target:
                return
            
            min_el_i = 0 if not arr else arr[-1]
            for i in range(min_el_i, len(candidates)):
                backtrack(arr + [i])
                
        backtrack([])
        newRes = []
        
        for arr in res:
            newRes.append([candidates[i] for i in arr])
        
        return newRes
                
                    
        