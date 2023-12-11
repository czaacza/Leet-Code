class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        queue = []
        for point in points:
            distance= math.dist((point[0], point[1]), (0,0))
            queue.append((distance, point))
        
        heapq.heapify(queue)
        res = []
        for i in range(k):
            res.append(heapq.heappop(queue)[1])
        
        return res
        
        