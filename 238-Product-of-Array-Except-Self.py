class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = [1]
        mul_rev = [1]
        for i in range(len(nums)):
            mul.append(mul[i] * nums[i])
            mul_rev.append(mul_rev[i] * nums[len(nums)-1 - i])

        res = []
        for i in range(len(nums)):
            res.append(mul[i] * mul_rev[len(nums)-1 - i])

        return res
        

        