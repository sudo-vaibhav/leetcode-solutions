class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ct = defaultdict(int)
        s = set(nums)
        for num in nums:
            
            if num+1 in s:
                ct[(num,num+1)]+=1
            if num-1 in s:
                ct[(num-1,num)]+=1
        if ct:
            return max(ct.values())
        return 0