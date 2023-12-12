class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ROWS = len(isConnected)
        COLS = len(isConnected[0])
        
        graph = {i : [] for i in range(1, len(isConnected) + 1)}
                
        for r in range(ROWS):
            for c in range(COLS):
                if isConnected[r][c] == 1 and r != c:
                    graph[r+1].append(c+1)
                
        def dfs(graph, visited, curr):
            if curr in visited:
                return
            
            visited.add(curr)
            
            for n in graph[curr]:
                if n not in visited:
                    dfs(graph, visited, n)
                    
        visited = set()
        count = 0
        for node in graph:
            if node not in visited:
                dfs(graph, visited, node)
                count += 1
        
        return count
            
        
        
            
        
        
                    
        