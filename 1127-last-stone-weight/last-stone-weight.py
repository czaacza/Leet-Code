class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            bigger = -heapq.heappop(heap)
            smaller = -heapq.heappop(heap)
            if bigger != smaller:
                heapq.heappush(heap, - (bigger - smaller))
        
        return -heap[0] if len(heap) == 1 else 0

        
        