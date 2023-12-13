class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ROWS = len(mat)
        COLS = len(mat[0])
        
        def search(r, c):
            curr_row = mat[r][:]
            for curr_c in range(len(curr_row)):
                if curr_c == c:
                    continue
                if curr_row[curr_c] == 1:
                    return False
            
            curr_col = [row[c] for row in mat]
            for curr_r in range(len(curr_col)):
                if curr_r == r:
                    continue
                if curr_col[curr_r] == 1:
                    return False
            
            
            return True
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 1:
                    if search(r, c) == True:
                        res += 1
                        
        return res
                        
            
                    
        
        
                        
            
            
                    
        