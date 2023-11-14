class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dist_x = abs(sx - fx)
        dist_y = abs(sy - fy)

        if dist_x == 0 and dist_y == 0 and t == 1:
            return False

        return dist_x <= t and dist_y <= t