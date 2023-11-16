class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums_set = set(nums)
        res = set()
        def backtrack(curr_str, curr_len):
            nonlocal res

            if curr_len == len(nums[0]):
                res.add(curr_str)
                return
            
            backtrack(curr_str + "0", curr_len+1)
            backtrack(curr_str + "1", curr_len+1)
        
        backtrack('', 0)

        for el in res:
            if el not in nums_set:
                return el
           


        