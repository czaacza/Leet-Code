class Solution:
    def totalMoney(self, n: int) -> int:
        
        week = 1
        total = 0
        weekDay = 1
        for _ in range(1, n+1):
            if weekDay > 7:
                week += 1
                weekDay = 1
            
            total += week + weekDay - 1
            weekDay += 1
            
        return total
        