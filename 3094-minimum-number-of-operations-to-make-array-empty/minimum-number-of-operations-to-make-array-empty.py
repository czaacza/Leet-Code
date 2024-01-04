class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_val = max(counter.values())
        dp = [0, math.inf]
        for i in range(2, max_val+1):
            three_before = dp[i-3] if i-3 >= 0 else math.inf
            two_before = dp[i-2]
            dp.append(min(three_before, two_before)+1)

        res = 0
        for val in counter.values():
            res += dp[val]
        
        return res if res != inf else -1





        

        