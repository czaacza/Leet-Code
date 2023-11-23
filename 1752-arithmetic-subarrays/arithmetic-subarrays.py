class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isArithmetic(arr):
            arr.sort()
            if len(arr) <= 2:
                return True
            diff = arr[1] - arr[0]
            for i in range(1, len(arr)):
                if arr[i] - arr[i-1] != diff:
                    return False
            return True
                
        res = []
        for i in range(len(l)):
            arr = nums[l[i]:r[i]+1]
            res.append(isArithmetic(arr))

        return res


        