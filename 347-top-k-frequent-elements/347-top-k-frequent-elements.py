class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)
        minH = []
        for key in ctr:
            heappush(minH,(ctr[key],key))
            if len(minH)>k:
                heappop(minH)
        return [x[1] for x in minH]
        