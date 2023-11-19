class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        seen = set()
        counter = 0
        operations = 0
        nums.sort()
        
        for n in nums:
            if n in seen:
                operations += counter-1
                continue
            seen.add(n)
            operations += counter
            counter += 1


        return operations


        

        