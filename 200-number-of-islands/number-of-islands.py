class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c, visited):
            def isOkay(r,c):
                if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                    return False
                if grid[r][c] != '1':
                    return False
                if (r,c) in visited:
                    return False
                return True
            
            if not isOkay(r,c):
                return

            visited.add((r,c))
            dfs(r+1, c, visited)
            dfs(r-1, c, visited)
            dfs(r, c+1, visited)
            dfs(r, c-1, visited)

        visited = set()
        counter = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] != '0':
                    dfs(r,c, visited)
                    counter+=1

        return counter
