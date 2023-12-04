class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_v = 0
        while l <= r:
            h = min(height[l], height[r])
            v = (r - l) * h
            max_v = max(max_v, v)
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return max_v
        