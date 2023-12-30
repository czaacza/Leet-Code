class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        all_letters = set()
        for word in words:
            for letter in word:
                if letter not in all_letters:
                    all_letters.add(letter)
        
        counters = []
        for word in words:
            curr_counter = {}
            counters.append(Counter(word))
        
        for letter in all_letters:
            for counter in counters:
                if letter not in counter:
                    counter[letter] = 0

        for letter in all_letters:
            while True:
                min_counter = math.inf
                min_counter_ind = 0

                max_counter = 0
                max_counter_ind = 0

                for i in range(len(counters)):
                    if counters[i][letter] < min_counter:
                        min_counter = counters[i][letter]
                        min_counter_ind = i

                    if counters[i][letter] > max_counter:
                        max_counter = counters[i][letter]
                        max_counter_ind = i
                    
                if min_counter == max_counter:
                    break
                    
                if max_counter == min_counter + 1:
                    return False    
                
                else:
                    counters[max_counter_ind][letter] -= 1
                    counters[min_counter_ind][letter] += 1

        return True


        