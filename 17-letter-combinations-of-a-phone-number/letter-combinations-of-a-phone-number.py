class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        mapping = [
            [],
            [], 
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z']
            ]
        
        letters = []
        for d in digits:
            letters.append(mapping[int(d)])
        
        res = []
        
        def comb(letters, res, lvl, curr_str):
            if lvl == len(letters):
                res.append(curr_str)
                return
            
            for letter in letters[lvl]:
                comb(letters, res, lvl + 1, curr_str + letter)        
        
        for letter in letters[0]:
            comb(letters, res, 1, letter)
            
        
        return res
            

        
                

