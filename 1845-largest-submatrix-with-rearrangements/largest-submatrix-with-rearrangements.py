class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        res = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if r > 0 and matrix[r][c] != 0:
                    matrix[r][c] += matrix[r-1][c]
        
        for r in range(ROWS):
            curr_row = sorted(matrix[r], reverse=True)
            for i in range(len(curr_row)):
                res = max(res, (i + 1) * curr_row[i])
                
        return res
        