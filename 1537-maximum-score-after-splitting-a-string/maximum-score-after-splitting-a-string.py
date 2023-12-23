class Solution:
    def maxScore(self, s: str) -> int:
        left_score = 1 if s[0] == '0' else 0
        right_score = 0
        for r in s[1:]:
            if r == '1':
                right_score += 1

        max_score = left_score + right_score
        
        for i in range(1, len(s)-1):
            if s[i] == '0':
                left_score += 1
            elif s[i] == '1':
                right_score -= 1
            
            max_score = max(max_score, left_score + right_score)
        
        return max_score
                
        