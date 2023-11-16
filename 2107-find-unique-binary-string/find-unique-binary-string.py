class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums_set = set(nums)
        res = None
        def backtrack(curr_str, curr_len):
            nonlocal res

            if curr_len == len(nums[0]):
                if curr_str not in nums_set:
                    res = curr_str
                return
            
            backtrack(curr_str + "0", curr_len+1)
            backtrack(curr_str + "1", curr_len+1)
        
        backtrack('', 0)
        
        return res
           


        