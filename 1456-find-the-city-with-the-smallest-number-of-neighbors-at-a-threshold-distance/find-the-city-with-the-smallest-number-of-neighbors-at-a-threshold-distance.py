class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []
        for e in edges:
            graph[e[0]].append([e[1], e[2]])
            graph[e[1]].append([e[0], e[2]])
                        
        def dijkstra(graph, start, maxDistance):
            
            queue = [[0, start]]
            shortest = {}
            
            while queue:
                dist, curr = heapq.heappop(queue)
                if curr in shortest:
                    continue
                    
                if dist > maxDistance:
                    continue
                    
                shortest[curr] = dist
                                
                if graph[curr] == []:
                    continue
                
                for next_curr, next_dist in graph[curr]:
                    heapq.heappush(queue, [next_dist + dist, next_curr])
                
            return len(shortest) - 1
        
        min_len = math.inf
        min_len_i = 0
        
        for i in range(n):
            curr_len = dijkstra(graph, i, distanceThreshold)
            if curr_len <= min_len:
                min_len = curr_len
                min_len_i = i
                
        return min_len_i
                
                
            
        