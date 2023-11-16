class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific_q = deque()
        atlantic_q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pacific_q.append((r,c))
                if r == ROWS-1 or c == COLS-1:
                    atlantic_q.append((r,c))

        def search(q, visited):
            def isOkay(curr):
                if curr[0] < 0 or curr[0] >= ROWS or curr[1] < 0 or curr[1] >= COLS:
                    return False
                return True

            while q:
                curr = q.pop()
                if curr in visited:
                    continue

                visited.add(curr)

                if not isOkay(curr):
                    continue
                
                if isOkay((curr[0] + 1, curr[1])) and heights[curr[0] + 1][curr[1]] >= heights[curr[0]][curr[1]]:
                    q.append((curr[0] + 1, curr[1]))
                if isOkay((curr[0] - 1, curr[1])) and heights[curr[0] - 1][curr[1]] >= heights[curr[0]][curr[1]]:
                    q.append((curr[0] - 1, curr[1]))
                if isOkay((curr[0], curr[1] + 1)) and heights[curr[0]][curr[1] + 1] >= heights[curr[0]][curr[1]]:
                    q.append((curr[0], curr[1] + 1))
                if isOkay((curr[0], curr[1] - 1)) and heights[curr[0]][curr[1] - 1] >= heights[curr[0]][curr[1]]:
                    q.append((curr[0], curr[1] - 1))    
                
        pacific_visited = set()
        search(pacific_q, pacific_visited)

        atlantic_visited = set()
        search(atlantic_q, atlantic_visited)
        
        res = []

        for el in pacific_visited:
            if el in atlantic_visited:
                res.append([el[0], el[1]])
        
        return res


        