class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [ [0] * (n+1) ] * (m + 1)
        matrix[1][1] = 1 
        for r in range(m):
            for c in range(n):
                matrix[r+1][c+1] = matrix[r][c+1] + matrix[r+1][c]                
                
        return matrix[-1][-1]
                
        