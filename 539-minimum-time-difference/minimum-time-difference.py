class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
    
        for i in range(len(timePoints)):
            hour, minutes = [int(x) for x in timePoints[i].split(':')]
            print('hour, minutes', hour, minutes)
            minutes_past_midnight = (hour * 60) + minutes
            timePoints[i] = minutes_past_midnight
        
        timePoints.sort()

        res = 1440 + timePoints[0] - timePoints[-1]

        for i in range(1, len(timePoints)):
            res = min(res, timePoints[i] - timePoints[i-1])
        
        return res




      



        