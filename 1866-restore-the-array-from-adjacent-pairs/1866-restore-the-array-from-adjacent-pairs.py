class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        def dfs(graph, curr, visited, nums):
            if curr in visited:
                return
            nums.append(curr)
            visited.add(curr)
            for node in graph[curr]:
                dfs(graph, node, visited, nums)

        adj = {}

        for pair in adjacentPairs:
            adj[pair[0]] = adj.get(pair[0], []) + [pair[1]]
            adj[pair[1]] = adj.get(pair[1], []) + [pair[0]]
        
        head = None
        for key in adj:
            if len(adj[key]) == 1:
                head = key
        
        visited = set()
        nums = []
        dfs(adj, head, visited, nums)

        return nums

