class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = {}
        for i in range(numCourses):
            graph[i] = []
        
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
        
        def dfs(curr, visited, cycle, output):
            if curr in cycle:
                return False
            if curr in visited:
                return True
            
            visited.add(curr)
            cycle.add(curr)
            
            for n in graph[curr]:
                    if dfs(n, visited, cycle, output) == False:
                        return False

            cycle.remove(curr)

            output.append(curr)
            return True
        
        visited = set()
        output = []
        for node in range(numCourses):
            if dfs(node, visited, set(), output) == False:
                return []

        return reversed(output)

            

        