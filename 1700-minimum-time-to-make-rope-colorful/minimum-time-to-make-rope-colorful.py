class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l, r = 0,0 
        res = 0

        while r < len(colors):
            curr_sum = 0
            max_time = 0
            while r < len(colors) and colors[l] == colors[r]:
                curr_sum += neededTime[r]
                max_time = max(max_time, neededTime[r])
                r += 1

            curr_sum -= max_time
            res += curr_sum

            l = r
        
        return res
        