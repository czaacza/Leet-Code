class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = {}

        for i in range(len(edges)):
            if edges[i][0] not in graph:
                graph[edges[i][0]] = []
            if edges[i][1] not in graph:
                graph[edges[i][1]] = []
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
        
        for node, neig in graph.items():
            if len(neig) > 1:
                return node
            
    

        