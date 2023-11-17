class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        max_pair_sum = -math.inf

        min_q, max_q = [n for n in nums], [n for n in nums]

        min_q.sort()
        max_q.sort(reverse=True)

        while min_q and max_q:
            min_el = min_q.pop()
            max_el = max_q.pop()

            max_pair_sum = max(max_pair_sum, min_el + max_el)
            
        
        return max_pair_sum

            

        