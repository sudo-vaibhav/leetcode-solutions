class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        sumMap = defaultdict(int)
        intvls = []
        sumMap[0] = -1
        pSum = 0
        for idx,num in enumerate(nums):
            pSum += num
            if pSum-target in sumMap:
                intvls.append((sumMap[pSum-target]+1,idx))
            sumMap[pSum] = idx#.append(idx)
        
        if not intvls:return 0
        # intvls.sort(key=lambda x :x[1])
        prev = intvls[0]
        ans = 1
        for i in range(1,len(intvls)):
            cur = intvls[i]
            if cur[0]>prev[1]:
                ans+=1
                prev = cur
            
        return ans