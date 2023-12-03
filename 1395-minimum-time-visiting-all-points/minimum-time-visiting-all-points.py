class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        j = 1
        counter = 0
        curr_point = points[0]
        while j < len(points):
            next_point = points[j]
            
            if next_point == curr_point:
                j += 1
                continue
            
            curr_point[0] += 1 if next_point[0] > curr_point[0] else -1 if next_point[0] < curr_point[0] else 0
            curr_point[1] += 1 if next_point[1] > curr_point[1] else -1 if next_point[1] < curr_point[1] else 0
            
            counter += 1
            
        return counter
                
            
            
            
            
        