class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        used_i = set()
        res = []
        while len(used_i) != len(nums):
            seen = set()
            temp = []
            for i in range(len((nums))):
                if nums[i] not in seen and i not in used_i:
                    used_i.add(i)
                    seen.add(nums[i])
                    temp.append(nums[i])
            res.append(temp)

        return res

        