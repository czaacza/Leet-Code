class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        max_pair_sum = -math.inf

        min_q, max_q = nums, [-n for n in nums]

        heapq.heapify(min_q)
        heapq.heapify(max_q)

        for n in nums:
            min_el = heapq.heappop(min_q)
            max_el = - heapq.heappop(max_q)

            max_pair_sum = max(max_pair_sum, min_el + max_el)
        
        return max_pair_sum

            

        