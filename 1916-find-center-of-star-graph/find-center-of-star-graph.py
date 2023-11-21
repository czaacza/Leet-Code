class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen = {}

        for i in range(len(edges)):
            seen[edges[i][0]] = seen.get(edges[i][0], 0) + 1
            seen[edges[i][1]] = seen.get(edges[i][1], 0) + 1

            if seen[edges[i][0]] > 1:
                return edges[i][0]
            elif seen[edges[i][1]] > 1:
                return edges[i][1]

            
    

        