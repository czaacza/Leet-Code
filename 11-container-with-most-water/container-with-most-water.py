class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_v = 0

        while l < r:
            leftEl, rightEl = height[l], height[r]
            h = min(leftEl, rightEl) 
            curr_v = h * (r - l)
            max_v = max(max_v, curr_v)

            if leftEl <= rightEl:
                l += 1
            else:
                r -= 1
        
        return max_v