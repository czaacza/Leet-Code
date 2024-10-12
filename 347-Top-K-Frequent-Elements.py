class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            if n not in counter:
                counter[n] = 0
            counter[n] += 1
        
        maks = max(counter.values())
        arr = [None] * (maks + 1)
        for key in counter:
            value = counter[key]
            if arr[value] is None:
                arr[value] = []
            arr[value].append(key)

        print('arr', arr)
        res = []
        for i in range(len(arr)-1, -1, -1):
            if arr[i] is None:
                continue
            if len(res) < k:
                for n in arr[i]:
                    res.append(n)
            if len(res) == k:
                return res

        return res

            