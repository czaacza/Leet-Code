class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ROWS = len(nums)
        COLS = len(nums[0])
        max_sum = (ROWS + COLS) * 2
        
        sums = [-1] * max_sum

        for r in range(ROWS-1, -1, -1):
            for c in range(len(nums[r])-1, -1, -1):
                suma = r + c
                if sums[suma] == -1:
                    sums[suma] = []
                sums[suma].append(nums[r][c])

        res = []
        for arr in sums:
            if arr == -1:
                continue
            for el in arr:
                res.append(el)

        return res


        