class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        to_pick = {}
        for s in garbage:
            for letter in s:
                to_pick[letter] = to_pick.get(letter, 0) + 1
        
        trucks = ['G', 'P', 'M']
        minutes = 0

        for truck in trucks:
            for i in range(len(garbage)):
                while truck in garbage[i]:
                    to_pick[truck] -= 1
                    minutes += 1
                    garbage[i] = garbage[i].replace(truck, '.', 1)
                
                if truck not in to_pick or to_pick[truck] == 0:
                    break

                if i < len(garbage) - 1:
                    minutes += travel[i]
            
        return minutes
                
            


        