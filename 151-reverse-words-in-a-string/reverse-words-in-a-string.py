class Solution:
    def reverseWords(self, s: str) -> str:
        arr = []
        splitted = s.split(' ')
        for i in range(len(splitted)-1, -1, -1):
            if splitted[i] is not '':
                arr.append(splitted[i])
        
        print('arr', arr)
        
        for i in range(len(arr)):
            if " " in arr[i]:
                arr[i] = ''
        
        return ' '.join(arr)
            
        