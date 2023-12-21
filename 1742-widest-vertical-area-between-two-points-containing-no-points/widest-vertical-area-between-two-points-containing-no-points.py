class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        points.sort()
        max_dist = 0
        for i in range(1, len(points)):
            if points[i][0] - points[i-1][0] > max_dist:
                max_dist = points[i][0] - points[i-1][0]
        
        return max_dist
        