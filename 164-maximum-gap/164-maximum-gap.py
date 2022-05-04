class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2:
            return 0
        hi,lo = max(nums),min(nums)
        if hi==lo: return 0
        bs = ceil((hi-lo)/(n-1))
        bucketCount = n-1
        
        buckets = defaultdict(list)
        for num in nums:
            i = (num-lo)//bs
            buckets[i].append(num)
        
        ans = bs
        # print(buckets)
        prev = buckets[0]
        for i in range(1,n):
            b2 = buckets[i]
            
            if len(b2):
                ans = max(ans,min(b2)-max(prev))
                prev = b2
        return ans
            