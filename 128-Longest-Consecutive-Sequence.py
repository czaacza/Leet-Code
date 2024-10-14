class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        visited = set()
        for n in nums:
            if n in visited:
                continue
            curr_res = 1
            curr_num_up = n+1
            curr_num_down = n-1
            while curr_num_up in nums_set:
                visited.add(curr_num_up)
                curr_num_up += 1
                curr_res += 1   

            while curr_num_down in nums_set:
                visited.add(curr_num_down)
                curr_num_down -= 1
                curr_res += 1

            res = max(res, curr_res)
        
        return res
        