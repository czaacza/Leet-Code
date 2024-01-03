class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ROWS = len(bank)
        COLS = len(bank[0])
        prev = []
        res = 0
        for r in range(ROWS):
            curr_row = bank[r]
            curr = []
            for el in curr_row:
                if el == '1':
                    curr.append(el)
            
            if len(curr) == 0:
                continue
            
            res += (len(prev) * len(curr))

            prev = curr.copy()

        return res


        