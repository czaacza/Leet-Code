class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)
        res = 0
        
        for word in words:
            curr_counter = counter.copy()
            
            for i in range(len(word)):
                if word[i] in curr_counter and curr_counter[word[i]] > 0:
                    curr_counter[word[i]] -= 1
                else:
                    break
                    
            else:
                print('found word', word)
                res += len(word)
        
        return res
                   
        