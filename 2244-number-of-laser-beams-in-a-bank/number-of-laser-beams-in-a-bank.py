class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ROWS = len(bank)
        COLS = len(bank[0])
        prev = 0
        res = 0
        for r in range(ROWS):
            curr_row = bank[r]
            curr = 0
            for el in curr_row:
                if el == '1':
                    curr += 1
            
            if curr == 0:
                continue
            
            res += (prev * curr)
            prev = curr

        return res


        