class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        diff = [[0 for i in range(COLS)] for j in range(ROWS)]
        
        ones_rows = [0 for i in range(ROWS)]
        ones_cols = [0 for i in range(COLS)]
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    ones_rows[r] += 1
                    ones_cols[c] += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                diff[r][c] = 2 * ones_rows[r] + 2 * ones_cols[c] - ROWS - COLS
        
        return diff
                
                        
                
        