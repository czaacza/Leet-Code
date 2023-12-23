class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr_pos = (0, 0)
        visited = set()
        visited.add(curr_pos)
        for sign in path:
            if sign == 'N':
                curr_pos = (curr_pos[0], curr_pos[1] + 1)
            elif sign == 'S':
                curr_pos = (curr_pos[0], curr_pos[1] - 1)
            elif sign == 'E':
                curr_pos =  (curr_pos[0] + 1, curr_pos[1])
            elif sign == 'W':
                curr_pos =  (curr_pos[0] - 1, curr_pos[1])
            
            if curr_pos in visited:
                return True
            
            visited.add(curr_pos)
        
        return False
            
            
            
            
        