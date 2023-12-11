class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        l, r = 0, 0
        while r <= len(arr) - 1:
            if arr[r] == arr[l]:
                if r - l + 1 > len(arr) / 4:
                    return arr[l]
            else:
                l = r
            r += 1
                
                
        