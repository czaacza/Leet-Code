class Solution:
    def largestGoodInteger(self, num: str) -> str:
        num = str(num)
        max_num = '-1'
        i = 0
        while i <= len(num)-3:
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                max_num = max(max_num, num[i])
                i += 3
                continue
                
            i += 1
            
        if max_num == '-1':
            return ""
        
        return str(max_num * 3)
                
            
            
        