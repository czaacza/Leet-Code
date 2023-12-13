class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ROWS = len(mat)
        COLS = len(mat[0])
        
        def search(r, c):
            curr_row = mat[r][:]
            print('search', r, c)
            print('curr_row', curr_row)
            for curr_c in range(len(curr_row)):
                if curr_c == c:
                    continue
                if curr_row[curr_c] == 1:
                    return False
            
            curr_col = [row[c] for row in mat]
            print('curr_col', curr_col)
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
                        print('extra res')
                        res += 1
                        
        return res
                        
            
                    
        
        
                        
            
            
                    
        