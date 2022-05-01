class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        m,n = len(nums),len(nums[0])
        
        heap = []
        maxInHeap = -inf
        for i in range(m):
            cur = nums[i][0]
            heappush(heap,(cur,i,0))
            maxInHeap = max(maxInHeap,cur)
        
        ans = [-10**5,10**5]
        
        while len(heap)>=m:
            smallestNum,listIdx,elemIdx = heappop(heap)
            if ans[1]-ans[0]>maxInHeap-smallestNum:
                ans = [smallestNum,maxInHeap]
            
            if elemIdx+1<len(nums[listIdx]):
                newVal = nums[listIdx][elemIdx+1]
                maxInHeap = max(maxInHeap,newVal)
                heappush(heap,(newVal,listIdx,elemIdx+1))
        return ans