class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_p = ['(', '{', '[']
        close_p = [')', '}', ']']
        
        for p in s:
            if p in open_p:
                stack.append(p)
                continue
            for i in range(len(close_p)):
                if p == close_p[i]:
                    if len(stack) == 0 or stack.pop() != open_p[i]:
                        return False
                    
        return len(stack) == 0
                    
                
            