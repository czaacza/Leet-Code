class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = {}
        for i in range(n):
            graph[i] = []
        
        for i in range(len(edges)):
            e = edges[i]
            graph[e[0]].append([e[1], succProb[i]])
            graph[e[1]].append([e[0], succProb[i]])        
        
        def dijkstra(graph, start, end):
            queue = [[-1, start]]
            longest = {}
            
            while queue:
                dist, curr = heapq.heappop(queue)
                dist = - dist
                if curr in longest:
                    continue
                longest[curr] = dist
                
                
                for next_curr, next_dist in graph[curr]:
                    heapq.heappush(queue, [-(dist * next_dist), next_curr])     
            
            return longest
                
        paths = dijkstra(graph, start_node, end_node)
        if end_node not in paths:
            return 0
        
        return paths[end_node]
                
            
        
        