class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        
        hp = []
        for i in count:
            heappush(hp,(count[i],i))
            if len(hp)>k:
                heappop(hp)
        
        return map(lambda x:x[1],hp)