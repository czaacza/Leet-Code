class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        
        queue = deque()
        queue.append((sr, sc))
        init_color = image[sr][sc]
        if init_color == color:
            return image

        while queue:
            curr = queue.popleft()
            def isOkay(curr):
                if curr[0] < 0 or curr[0] >= ROWS or curr[1] < 0 or curr[1] >= COLS:
                    return False
                return True
            
            if not isOkay(curr):
                continue
            
            if image[curr[0]][curr[1]] != init_color:
                continue
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                next_node = (curr[0] + dx, curr[1] + dy)
                if isOkay(next_node):
                    queue.append(next_node)
        
            image[curr[0]][curr[1]] = color
        
        return image
            
        
        
        
        