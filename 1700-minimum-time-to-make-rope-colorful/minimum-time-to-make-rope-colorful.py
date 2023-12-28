class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < len(colors):
            curr_heap = []
            while r < len(colors) and colors[r] == colors[l]:
                heapq.heappush(curr_heap, neededTime[r])
                r += 1
            found = heapq.nsmallest(r - l - 1, curr_heap)
            for f in found:
                res += f  

            l = r        

        return res


        