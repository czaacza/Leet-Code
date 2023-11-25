class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def is_overlap(first, second):
            if second[1] < first[0] or second[0] > first[1]:
                return False
            return True
        
        intervals.sort()
        stack = [intervals[0]]

        
        for i in range(1, len(intervals)):
            if len(stack) > 0:
                if is_overlap(intervals[i], stack[-1]):
                    stack[-1] = [min(intervals[i][0], stack[-1][0]), max(intervals[i][1], stack[-1][1])]
                else:
                    stack.append(intervals[i])
        
        return stack
            
            