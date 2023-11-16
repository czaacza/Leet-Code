class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for el in prerequisites:
            adj[el[0]] = adj.get(el[0], []) + [el[1]]

        canAllBeDone = True
        def dfs(curr, visited): 
            nonlocal canAllBeDone
            if curr not in adj or adj[curr] == []:
                return

            if curr in visited:
                canAllBeDone = False
                return
            visited.add(curr)

            for n in adj[curr]:
                dfs(n, visited)
            
            visited.remove(curr)
            adj[curr] = []


        for n in range(numCourses):
            dfs(n, set())
            if canAllBeDone == False:
                return False

        return True


                        
        
