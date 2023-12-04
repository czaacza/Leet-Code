class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for i in range(n+1):
            graph[i] = []
            
        for u, v, w in times:
            graph[u].append([v, w])
                
        def bfs(graph, start):
            shortest = {}
            queue = [[0, start]]
            
            while queue:
                dist, curr = heapq.heappop(queue)
                if curr in shortest:
                    continue
                    
                shortest[curr] = dist
                
                if graph[curr] == []:
                    continue
                    
                for next_curr, next_dist in graph[curr]:
                    heapq.heappush(queue, [next_dist + dist, next_curr])
            
            return shortest
        
        paths = bfs(graph, k)
        if len(paths) != n:
            return -1
        
        return max(paths.values())
                    
                
                
            
            
        